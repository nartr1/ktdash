from pydantic import BaseModel
from typing import List
import datetime
from models.roster import Roster

class User(BaseModel):
    userid: str
    username: str
    passhash: str
    createddate: datetime
    rosters: List[Roster]