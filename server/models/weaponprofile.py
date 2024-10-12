from pydantic import BaseModel
from typing import List

class WeaponProfile(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    wepid: str
    profileid: str
    name: str
    A: str
    BS: str
    D: str
    SR: str
