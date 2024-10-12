from pydantic import BaseModel

class Equipment(BaseModel):
    factionid: str
    killteamid: str
    fireteamid: str
    opid: str
    eqid: str
    #: Ordering sequence for this equipment
    eqseq: int
    eqpts: str
    eqname: str
    eqdescription: str
    #: Equipment variables for auto-applying mods
    eqtype: str | None
    eqvar1: str | None
    eqvar2: str | None
    eqvar3: str | None
    eqvar4: str | None
    #: Category for this Equipment, e.g. "Equipment", "Universal Equipment", "Battle Honour", etc.
    eqcategory: str

    class Config:
        orm_mode=True

    @staticmethod
    def from_orm(orm_row, session):
        return Equipment(
            factionid=orm_row.factionid,
            killteamid=orm_row.killteamid,
            fireteamid=orm_row.fireteamid,
            opid=orm_row.opid,
            eqid=orm_row.eqid,
            eqseq=orm_row.eqseq,
            eqpts=orm_row.eqpts,
            eqname=orm_row.eqname,
            eqdescription=orm_row.eqdescription,
            eqtype=orm_row.eqtype,
            eqvar1=orm_row.eqvar1,
            eqvar2=orm_row.eqvar2,
            eqvar3=orm_row.eqvar3,
            eqvar4=orm_row.eqvar4,
            eqcategory=orm_row.eqcategory,
        )