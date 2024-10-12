from pydantic import BaseModel
from typing import List

class Ploy(BaseModel):
    factionid: str
    killteamid: str
    #: PloyTypes: S for Strategic, T for Tactical (Firefight in kt24)
    ploytype: str
    ployid: str
    ployname: str
    CP: str
    description: str

class Ploys(BaseModel):
    strat: List[Ploy]
    tac: List[Ploy]
