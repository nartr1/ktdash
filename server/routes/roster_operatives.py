from typing import Annotated

from api.user.rosteroperative import RosterOperativeAPI
from api.user.user import get_current_user_with_session
from db.engine import SessionDep
from fastapi import Depends, APIRouter
from models.rosteroperative import AddRosterOperative
from models.user import User

roster_op_router = APIRouter(prefix="/api/roster_operatives")


@roster_op_router.post("/{roster_id}/operatives")
def add_roster_operative(
    roster_id: str,
    roster_operative_args: AddRosterOperative,
    current_user: Annotated[User, Depends(get_current_user_with_session)],
):
    """
    Test path: /api/rosters/862286e7-0464-46bc-99e1-3b8b270b82b0/operatives
    Test body:
    {
        "baseopid": "GNR",
        "opname": "testop",
        "factionid": "IMP",
        "killteamid": "GK",
        "fireteamid": "GK",
        "wepids": "F,INC,PSC,PSL",
        "eqids": "PS,TSA"
    }
    """
    # Add a new operative to the roster
    new_operative = RosterOperativeAPI.create_roster_operative(
        roster_id, roster_operative_args, current_user[0], current_user[1]
    )
    return new_operative


@roster_op_router.put("/{roster_id}/operatives/{opertative_id}")
def update_roster_operative(roster_id: str, operative_id: str, session: SessionDep):
    # Update the operative with the given ID in the roster

    # Implement your logic here to update the operative in the roster
    pass


@roster_op_router.delete("/{roster_id}/operatives/{opertative_id}")
def delete_roster_operative(roster_id: str, operative_id: str, session: SessionDep):
    # Delete the operative with the given ID from the roster
    pass
