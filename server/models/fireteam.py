from pydantic import BaseModel
from typing import List

from sqlmodel import select
from db.schema import Operative as OperativeDB

from models.operative import Operative

class Fireteam(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    description: str | None
    fireteamname: str
    archetype: str | None
    fireteamcomp: str
    operatives: List[Operative]

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        operatives = select(OperativeDB).where(OperativeDB.factionid == orm_row.factionid, OperativeDB.killteamid == orm_row.killteamid)
        operatives = session.exec(operatives).all()

        return Fireteam(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            description=orm_row.description,
            fireteamname=orm_row.fireteamname,
            archetype=orm_row.archetype,
            fireteamcomp=orm_row.fireteamcomp,
            operatives=[Operative.from_orm(row, session) for row in operatives]
        )