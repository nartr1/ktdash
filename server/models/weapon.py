from pydantic import BaseModel
from typing import List

from models.weaponprofile import WeaponProfile

class Weapon(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    wepid: str
    wepname: str
    #: Weapon types: M (melee), R (ranged), P (psychic), E (Equipment)
    weptype: str
    weaponprofiles: List[WeaponProfile]

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return Weapon(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            wepid=orm_row.wepid,
            wepname=orm_row.wepname,
            weptype=orm_row.weptype,
            weaponprofiles=[WeaponProfile.from_orm(orm_row, session) for orm_row in orm_row.weaponprofiles],
        )