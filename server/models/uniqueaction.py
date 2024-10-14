from pydantic import BaseModel

class UniqueAction(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    uniqueactionid: str
    AP: int
    title: str
    description: str
    
    class Config:
        orm_mode=True
    
    @staticmethod
    def from_orm(orm_row, session):
        return UniqueAction(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            uniqueactionid=orm_row.uniqueactionid,
            AP=orm_row.AP,
            title=orm_row.title,
            description=orm_row.description
        )