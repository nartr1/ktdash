import uuid
from typing import List

from db.schema import (
    Equipment,
    Operative,
    Roster,
    RosterOperative,
    User,
    Weapon,
    WeaponProfile,
)
from models.rosteroperative import AddRosterOperative
from sqlmodel import select


class RosterOperativeAPI:

    # rosterid: str
    # baseopid: str
    # opname: str
    # factionid: str
    # killteamid: str
    # fireteamid: str
    # opid: str
    # wepids: str
    # eqids: str
    @staticmethod
    def create_roster_operative(
        roster_id: str, roster_operative_args: AddRosterOperative, user: User, session
    ):
        # Create a new roster operative
        query = (
            select(Roster)
            .where(Roster.userid == user.userid)
            .where(Roster.rosterid == roster_id)
        )
        roster_row = session.exec(query).first()
        if roster_row is None:
            return None

        query = select(Operative, Weapon, Equipment).where(
            Operative.factionid == roster_row.factionid,
            Operative.killteamid == roster_row.killteamid,
            Operative.opid == roster_operative_args.baseopid,
            Weapon.factionid == roster_row.factionid,
            Weapon.killteamid == roster_row.killteamid,
            Weapon.opid == roster_operative_args.baseopid,
            WeaponProfile.factionid == roster_row.factionid,
            WeaponProfile.killteamid == roster_row.killteamid,
            WeaponProfile.opid == roster_operative_args.baseopid,
            Equipment.factionid == roster_row.factionid,
            Equipment.killteamid == roster_row.killteamid,
        )
        rows = session.exec(query).fetchall()

        if rows is None or len(rows) == 0:
            return None

        base_operative = rows[0][0]
        weapons = {row[1].wepid: row[1] for row in rows[0:]}
        equipment = {row[2].eqid: row[2] for row in rows[0:]}

        new_roster_operative = RosterOperative(
            userid=user.userid,
            rosterid=roster_id,
            rosteropid=uuid.uuid4(),
            factionid=roster_row.factionid,
            killteamid=roster_row.killteamid,
            fireteamid=base_operative.fireteamid,
            opid=base_operative.opid,
            opname=roster_operative_args.opname,
            wepids=roster_operative_args.wepids,
            eqids=roster_operative_args.eqids,
        )
        if not RosterOperativeAPI._validate_roster_operative(
            roster_row, new_roster_operative, base_operative, weapons, equipment
        ):
            return None
        session.add(new_roster_operative)
        session.commit()
        session.refresh(new_roster_operative)
        return new_roster_operative

    @staticmethod
    def _validate_roster_operative(
        current_roster: Roster,
        new_roster_operative: RosterOperative,
        base_operative: Operative,
        weapons: List[Weapon] = None,
        equipment: List[Equipment] = None,
    ):
        # Ensure the csv weapids and eqids are valid
        weapon_ids = new_roster_operative.wepids.split(",")
        equipment_ids = new_roster_operative.eqids.split(",")

        if len(weapon_ids) > 0:
            for weapon_id in weapon_ids:
                if weapon_id not in weapons:
                    return False
        else:
            return False

        if len(equipment_ids) > 0:
            for equipment_id in equipment_ids:
                if equipment_id not in equipment or (
                    equipment[equipment_id].opid != ""
                    and equipment[equipment_id].opid != base_operative.opid
                ):
                    return False

        # Ensure new operative does not exceed the fireteam maximum
        if base_operative.fireteammax > 0:
            current_count = 0
            for roster_op in current_roster.operatives:
                if roster_op.opid == base_operative.opid:
                    current_count += 1
            if current_count == base_operative.fireteammax:
                return False
        return True
