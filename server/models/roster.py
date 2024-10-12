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
    TP: int
    CP: int
    VP: int
    RP: int
    spotlight: int
    hascustomportrait: int
    portraitcopyok: int
    viewcount: int
    importcound: int
    ployids: str
    tacopids: str
    reqpts: int
    stratnotes: str
    eqnotes: str
    specopnotes: str
    createddate: datetime
    operatives: List[RosterOperative]