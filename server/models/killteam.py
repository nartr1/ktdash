from pydantic import BaseModel
from typing import List

from models.equipment import Equipment
from models.fireteam import Fireteam
from models.ploys import Ploys

class Killteam(BaseModel):
    factionid: str
    killteamid: str
    killteamname: str
    description: str
    killteamcomp: str
    equipments: List[Equipment]
    ploys: Ploys
    fireteams: List[Fireteam]