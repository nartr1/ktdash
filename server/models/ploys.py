from pydantic import BaseModel
from typing import List

class Ploy(BaseModel):
    factionid: str
    killteamid: str
    #: PloyTypes: S for Strategic, T for Tactical (Firefight in kt24)
    ploytype: str
    ployid: str
    ployname: str
    CP: str
    description: str

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return Ploy(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            ploytype=orm_row.ploytype,
            ployid=orm_row.ployid,
            ployname=orm_row.ployname,
            CP=orm_row.CP,
            description=orm_row.description
        )

class Ploys(BaseModel):
    strat: List[Ploy]
    tac: List[Ploy]

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return Ploys(
            strat=[Ploy.from_orm(row, session) for row in orm_row if row.ploytype == 'S'],
            tac=[Ploy.from_orm(row, session) for row in orm_row if row.ploytype == 'T']
        )