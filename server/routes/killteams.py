from fastapi import APIRouter
from db.engine import SessionDep
from db.schema import Faction, Killteam, Equipment, Fireteam
from sqlmodel import select
from models.faction import Faction as FactionResp
from typing import List
from fastapi.encoders import jsonable_encoder

from util.transformers import rows_as_dicts

killteams_router = APIRouter(prefix="/api")

@killteams_router.get("/faction", response_model=List[FactionResp])
def get_faction(session: SessionDep,fa: str | None = None):
    # Return the requested faction
    faction_id = fa
    if faction_id:
        statement = select(Faction).where(Faction.factionid == fa).where(Faction.factionid == Killteam.factionid)
    else:
        statement = select(Faction)

    result = session.exec(statement)
    faction_results = result.fetchall()
    
    response = [FactionResp.from_orm(row, session) for row in faction_results]

    return response

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
