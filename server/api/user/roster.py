import uuid

from db.schema import RosterOperative, Roster, User
from models.roster import CreateRoster, Roster as RosterModel
from sqlmodel import select


class RosterAPI:

    @staticmethod
    def get_roster(roster_id: str, session):
        query = select(Roster, RosterOperative).where(
            Roster.rosterid == roster_id, RosterOperative.rosterid == roster_id
        )
        roster_rows = session.exec(query).fetchall()

        if roster_rows is None or len(roster_rows) == 0:
            return None

        roster = roster_rows[0][0]
        operatives = {row[1].opid: row[1].dict() for row in roster_rows}

        return RosterModel(
            **roster.dict(),
            operatives=list(operatives.values()),
        )

    @staticmethod
    def create_roster(roster_args: CreateRoster, user: User, session):
        # Create a new roster
        query = (
            select(Roster)
            .where(Roster.userid == user.userid)
            .where(Roster.rostername == roster_args.rostername)
        )
        roster_row = session.exec(query).first()
        if roster_row is not None:
            return None

        new_roster = Roster(
            rosterid=uuid.uuid4(),
            userid=user.userid,
            rostername=roster_args.rostername,
            factionid=roster_args.factionid,
            killteamid=roster_args.killteamid,
        )
        session.add(new_roster)
        session.commit()
        session.refresh(new_roster)
        return new_roster

    @staticmethod
    def update_roster(user: User):
        pass

    @staticmethod
    def delete_roster(user: User):
        pass
