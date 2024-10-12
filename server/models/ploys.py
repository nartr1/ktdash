from pydantic import BaseModel
from typing import List

class Ploy(BaseModel):
    factionid: str
    killteamid: str
    ploytype: str
    ployid: str
    ployname: str
    CP: str
    description: str

class Ploys(BaseModel):
    strat: List[Ploy]
    tac: List[Ploy]
