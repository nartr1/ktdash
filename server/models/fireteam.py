from pydantic import BaseModel
from typing import List

from models.operative import Operative

class Fireteam(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    description: str
    fireteamname: str
    archetype: str
    fireteamcomp: str
    operatives: List[Operative]