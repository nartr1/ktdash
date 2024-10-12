from pydantic import BaseModel
from typing import List

from models.weapon import Weapon

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