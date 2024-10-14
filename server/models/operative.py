from pydantic import BaseModel
from typing import List

from sqlmodel import select
from db.schema import Weapon as WeaponDB
from db.schema import Equipment as EquipmentDB
from db.schema import UniqueAction as UniqueActionDB
from db.schema import Ability as AbilityDB

from models.weapon import Weapon
from models.equipment import Equipment
from models.uniqueaction import UniqueAction
from models.ability import Ability

class Operative(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    opname: str
    description: str
    M: str
    APL: str
    GA: str
    DF: str
    SV: str
    W: str
    weapons: List[Weapon]
    equipments: List[Equipment]
    uniqueactions: List[UniqueAction]
    abilities: List[Ability]

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        weapons = select(WeaponDB).where(WeaponDB.factionid == orm_row.factionid, WeaponDB.killteamid == orm_row.killteamid, WeaponDB.fireteamid == orm_row.fireteamid, WeaponDB.opid == orm_row.opid)
        weapons = session.exec(weapons).all()

        equipment = select(EquipmentDB).where(EquipmentDB.factionid == orm_row.factionid, EquipmentDB.killteamid == orm_row.killteamid, EquipmentDB.fireteamid == orm_row.fireteamid, EquipmentDB.opid == orm_row.opid)
        equipment = session.exec(equipment).all()

        return Operative(   
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            opname=orm_row.opname,
            description=orm_row.description,
            M=orm_row.M,
            APL=orm_row.APL,
            GA=orm_row.GA,
            DF=orm_row.DF,
            SV=orm_row.SV,
            W=orm_row.W,
            weapons=[Weapon.from_orm(row, session) for row in weapons],
            equipments=[Equipment.from_orm(row, session) for row in equipment],
            uniqueactions=[UniqueAction.from_orm(row, session) for row in orm_row.uniqueactions],
            abilities=[Ability.from_orm(row, session) for row in orm_row.abilities]
        )