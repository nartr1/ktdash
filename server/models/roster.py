from pydantic import BaseModel
from typing import List
import datetime
from models.rosteroperative import RosterOperative

class Roster(BaseModel):
    userid: str
    rosterid: str
    seq: int
    rostername: str
    factionid: str
    killteamid: str
    notes: str
    keyword: str
    #: Turning Point
    TP: int
    #: Command Points
    CP: int
    #: Victory Points
    VP: int
    #: Resource Points (e.g. Faith Points for Novitiates)
    RP: int
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