from pydantic import BaseModel
from typing import List

class Faction(BaseModel):
    factionid: str
    factionname: str
    description: str
    killteams: List[Killteam]