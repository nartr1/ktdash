import uuid

from db.schema import Roster, User
from models.roster import CreateRoster
from sqlmodel import select


class RosterAPI:

    @staticmethod
    def get_roster(roster_id: str, session):
        query = select(Roster).where(Roster.rosterid == roster_id)
        roster_row = session.exec(query).fetchall()
        if roster_row is None or len(roster_row) == 0:
            return None
        return roster_row

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
