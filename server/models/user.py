from datetime import datetime
from typing import List
from pydantic import BaseModel
from models.roster import Roster


class User(BaseModel):
    userid: str
    username: str
    createddate: datetime
    rosters: List[Roster]

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    userid: str | None = None


class UserInDB(User):
    passhash: str
