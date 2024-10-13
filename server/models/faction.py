from typing import List

from models.killteam import KillteamShort
from pydantic import BaseModel


class Faction(BaseModel):
    factionid: str
    factionname: str
    description: str
    killteams: List[KillteamShort]

    class Config:
        orm_mode = True

    @staticmethod
    def from_orm(orm_row, session):
        killteams = []

        for row in orm_row.killteams:
            killteams.append(
                KillteamShort(
                    killteamid=row.killteamid,
                    killteamname=row.killteamname,
                    killteamversion=row.edition,
                )
            )

        return Faction(
            factionid=orm_row.factionid,
            factionname=orm_row.factionname,
            description=orm_row.description,
            killteams=killteams,
        )
