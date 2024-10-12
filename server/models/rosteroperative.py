from pydantic import BaseModel
from typing import List

from models.operative import Operative
from models.weapon import Weapon
from models.equipment import Equipment

class Fireteam(BaseModel):
    rosterid: str
    userid: str
    rosteropid: str
    seq: int
    opname: str
    hascustomportrait: int

    factionid: str
    killteamid: str
    fireteamid: str
    opid: str

    wepids: str
    eqids: str
    curW: int
    isactivated: int
    isinjured: int
    hidden: int
    specialism: str

    baseoperative: Operative
    weapons: List[Weapon]
    equipments: List[Equipment]