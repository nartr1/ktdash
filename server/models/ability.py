from pydantic import BaseModel

class Ability(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    abilityid: str
    title: str
    description: str

    @staticmethod
    def from_orm(orm_row, session):
        return Ability(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            abilityid=orm_row.abilityid,
            title=orm_row.title,
            description=orm_row.description
        )