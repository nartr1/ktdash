from pydantic import BaseModel
from typing import List

class WeaponProfile(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    wepid: str
    profileid: int
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
