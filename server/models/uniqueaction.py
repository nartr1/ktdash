from pydantic import BaseModel

class UniqueAction(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    uniqueactionid: str
    AP: str
    title: str
    description: str