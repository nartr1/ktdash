from pydantic import BaseModel, Field
from typing import List
from models.killteam import Killteam

class Faction(BaseModel):
    factionid: str
    factionname: str
    description: str
    killteams: List[Killteam]
    
    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return Faction(
            factionid=orm_row.factionid,
            factionname=orm_row.factionname,
            description=orm_row.description,
            killteams=[Killteam.from_orm(row, session) for row in orm_row.killteams]
        )