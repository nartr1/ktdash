from fastapi import APIRouter
from db.engine import SessionDep
from db.schema import Faction, Killteam, Equipment, Fireteam, Operative
from sqlmodel import select

from models.faction import Faction as FactionResp
from models.killteam import Killteam as KillteamResp
from models.fireteam import Fireteam as FireteamResp
from models.operative import Operative as OperativeResp

from typing import List
from fastapi.encoders import jsonable_encoder

killteams_router = APIRouter(prefix="/api")

@killteams_router.get("/faction", response_model=List[FactionResp])
def get_faction(session: SessionDep,fa: str | None = None):
    # Return the requested faction
    if fa is None:
        statement = select(Faction)
    else:
        statement = select(Faction).where(Faction.factionid == fa)

    result = session.exec(statement)
    faction_results = result.fetchall()
    
    response = [FactionResp.from_orm(row, session) for row in faction_results]

    return response

@killteams_router.get("/killteam", response_model=List[KillteamResp])
def get_killteam(session: SessionDep,kt: str = None):
    # Return the requested killteam
    killteam_id = kt

    statement = select(Killteam).where(Killteam.killteamid == kt)

    result = session.exec(statement)
    killteam_results = result.fetchall()
    
    response = [KillteamResp.from_orm(row, session) for row in killteam_results]

    return response


@killteams_router.get("/fireteam", response_model=List[FireteamResp])
def get_fireteam(session: SessionDep, ft: str):
    # Return the requested fireteam

    statement = select(Fireteam).where(Fireteam.fireteamid == ft)
    
    result = session.exec(statement)
    fireteam_results = result.fetchall()
    
    response = [FireteamResp.from_orm(row, session) for row in fireteam_results]

    return response



@killteams_router.get("/operative", response_model=List[OperativeResp])
def get_operative(session: SessionDep, op: str):
    # Return the requested operative

    statement = select(Operative).where(Operative.opid == op)

    result = session.exec(statement)
    operative_results = result.fetchall()
    
    response = [OperativeResp.from_orm(row, session) for row in operative_results]

    return response
