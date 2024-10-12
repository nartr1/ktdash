from pydantic import BaseModel
from typing import List

class WeaponProfile(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    wepid: str
    profileid: str
    #: WeaponProfile name is only shown for weapons that have more than 1 profile
    name: str
    #: Number of Attacks (Atk in kt24)
    A: str
    #: Skill level - BS/WS (Hit in kt24)
    BS: str
    #: Damage (Dam in kt24)
    D: str
    #: Special rules, comma-separated (weapon rules in kt24)
    SR: str

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return WeaponProfile(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            wepid=orm_row.wepid,
            profileid=orm_row.profileid,
            name=orm_row.name,
            A=orm_row.A,
            BS=orm_row.BS,
            D=orm_row.D,
            SR=orm_row.SR
        )