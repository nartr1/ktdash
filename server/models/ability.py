from pydantic import BaseModel

class Ability(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    abilityid: str
    title: str
    description: str