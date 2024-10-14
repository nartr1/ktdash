from typing import List

from models.equipment import Equipment
from models.operative import Operative
from models.weapon import Weapon
from pydantic import BaseModel


class AddRosterOperative(BaseModel):
    baseopid: str
    opname: str
    factionid: str
    killteamid: str
    fireteamid: str
    wepids: str
    eqids: str


class RosterOperativeShort(BaseModel):
    rosteropid: str
    opname: str

    baseoperative: Operative
    wepids: str
    eqids: str

    specialism: str


class RosterOperative(BaseModel):
    rosterid: str
    userid: str
    rosteropid: str
    seq: int
    opname: str
    #: 0/1. 1 means this RosterOperative has a custom portrait image file
    hascustomportrait: int

    factionid: str
    killteamid: str
    fireteamid: str
    opid: str

    #: Comma-separated list of Weapon IDs (wepid) selected for this RosterOperative
    wepids: str
    #: Comma-separated list of Equipment IDs (eqid) selected for this RosterOperative
    eqids: str
    #: Current number of Wounds for this RosterOperative
    curW: int
    #: 0/1. 1 indicates this RosterOperative has been activated in its Roster's current Turning Point (TP)
    isactivated: int
    isinjured: int
    hidden: int
    specialism: str

    baseoperative: Operative
    weapons: List[Weapon]
    equipments: List[Equipment]

    class Config:
        orm_mode = True
