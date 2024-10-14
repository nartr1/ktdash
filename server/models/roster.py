from pydantic import BaseModel
from typing import List
from datetime import datetime

from models.rosteroperative import RosterOperative


class CreateRoster(BaseModel):
    rostername: str
    factionid: str
    killteamid: str


class Roster(BaseModel):
    userid: str
    rosterid: str
    seq: int
    rostername: str
    factionid: str
    killteamid: str
    keyword: str
    #: Turning Point
    TP: int | None
    #: Command Points
    CP: int | None
    #: Victory Points
    VP: int | None
    #: Resource Points (e.g. Faith Points for Novitiates)
    RP: int | None
    #: 0/1. 1 means this roster has been spotlighted
    spotlight: int
    #: 0/1. 1 means this roster has a custom portrait image
    hascustomportrait: int
    #: 0/1. 1 means when this roster is imported by another user, the roster and operative portraits should also be copied
    portraitcopyok: int
    viewcount: int
    importcount: int
    #: Comma-separated list of Ploy IDs currently in use by this roster
    ployids: str
    #: Comma-separated list of TacOp IDs currently in use by this roster
    tacopids: str
    #: Requisition points for narrative play
    reqpts: int
    stratnotes: str
    eqnotes: str
    specopnotes: str
    createddate: datetime
    operatives: List[RosterOperative]

    class Config:
        orm_mode = True
