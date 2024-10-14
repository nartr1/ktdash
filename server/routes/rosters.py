from typing import Annotated
from fastapi import APIRouter, Depends
from db.engine import SessionDep
from models.user import User
from models.roster import CreateRoster
from api.user.user import get_current_user_with_session
from api.user.roster import RosterAPI

rosters_router = APIRouter(prefix="/api/rosters")


@rosters_router.get("/")
def get_rosters(session: SessionDep):
    # Return a list of all rosters
    pass


@rosters_router.post("/")
def create_roster(
    roster: CreateRoster,
    current_user: Annotated[User, Depends(get_current_user_with_session)],
):
    # Create a new roster
    return RosterAPI.create_roster(roster, current_user[0], current_user[1])


@rosters_router.get("/{roster_id}")
def get_roster(
    roster_id: str,
    session: SessionDep,
):
    # Return the roster with the given ID
    return RosterAPI.get_roster(roster_id, session)


@rosters_router.put("/{roster_id}")
def update_roster(roster_id: str, session: SessionDep):
    # Update the roster with the given ID

    # Implement your logic here to update the roster
    pass


@rosters_router.delete("/{roster_id}")
def delete_roster(roster_id: str, session: SessionDep):
    # Delete the roster with the given ID
    pass
