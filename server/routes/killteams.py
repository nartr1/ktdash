from fastapi import APIRouter
from db.engine import SessionDep
from db.schema import Faction
from sqlmodel import select

killteams_router = APIRouter(prefix="/api")


@killteams_router.get("/faction")
def get_factions(session: SessionDep):
    # Return an array of all factions
    statement = select(Faction)
    result = session.exec(statement)

    results = result.fetchall()

    return results


@killteams_router.get("/faction")
def get_faction(fa: str, session: SessionDep):
    # Return the requested faction
    faction_id = fa
    # Implement your logic here to fetch the faction with the given ID
    pass


@killteams_router.get("/killteam")
def get_killteams(session: SessionDep):
    # Return an array of all killteams
    pass


@killteams_router.get("/killteam")
def get_killteam(fa: str, kt: str, session: SessionDep):
    # Return the requested killteam
    faction_id = fa
    killteam_id = kt
    # Implement your logic here to fetch the killteam with the given IDs
    pass


@killteams_router.get("/fireteam")
def get_fireteams(session: SessionDep):
    # Return an array of all fireteams
    pass


@killteams_router.get("/fireteam")
def get_fireteam(fa: str, kt: str, ft: str, session: SessionDep):
    # Return the requested fireteam
    faction_id = fa
    killteam_id = kt
    fireteam_id = ft
    # Implement your logic here to fetch the fireteam with the given IDs
    pass


@killteams_router.get("/operative")
def get_operatives(session: SessionDep):
    # Return an array of all operatives
    pass


@killteams_router.get("/operative")
def get_operative(fa: str, kt: str, ft: str, op: str, session: SessionDep):
    # Return the requested operative
    faction_id = fa
    killteam_id = kt
    fireteam_id = ft
    operative_id = op
    # Implement your logic here to fetch the operative with the given IDs
    pass
