from pydantic import BaseModel
from typing import List

from sqlmodel import select
from db.schema import Equipment as EquipmentDB

from models.equipment import Equipment
from models.fireteam import Fireteam
from models.ploys import Ploys


class KillteamShort(BaseModel):
    killteamid: str
    killteamname: str
    killteamversion: str | None

class Killteam(BaseModel):
    factionid: str
    killteamid: str
    killteamname: str
    description: str | None
    killteamcomp: str | None
    equipments: List[Equipment] | None
    ploys: Ploys | None
    fireteams: List[Fireteam] | None

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        equipment = select(EquipmentDB).where(EquipmentDB.factionid == orm_row.factionid, EquipmentDB.killteamid == orm_row.killteamid)
        equipment = session.exec(equipment).all()
        
        return Killteam(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            killteamname=orm_row.killteamname,
            description=orm_row.description,
            killteamcomp=orm_row.killteamcomp,
            equipments=[Equipment.from_orm(row, session) for row in equipment],
            ploys=Ploys.from_orm(orm_row.Ploy, session),
            fireteams=[Fireteam.from_orm(row, session) for row in orm_row.Fireteam]
        )