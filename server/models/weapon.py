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
    weptype: str
    weaponprofiles: List[WeaponProfile]