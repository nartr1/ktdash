from pydantic import BaseModel

class Equipment(BaseModel):
    factionid: str
    killteamid: str
    eqid: str
    eqpts: str
    eqname: str
    eqdescription: str