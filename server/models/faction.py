from pydantic import BaseModel, Field
from typing import List

class Faction(BaseModel):
    factionid: str
    factionname: str
    description: str
    killteamids: List[str]
    killteamnames: List[str]
    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        killteamids = []
        killteamnames = []

        for row in orm_row.killteams:
            killteamids.append(row.killteamid)
            killteamnames.append(row.killteamname)

        return Faction(
            factionid=orm_row.factionid,
            factionname=orm_row.factionname,
            description=orm_row.description,
            killteamids=killteamids,
            killteamnames=killteamnames
        )