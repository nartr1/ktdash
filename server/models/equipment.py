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
    eqtype: str
    eqvar1: str
    eqvar2: str
    eqvar3: str
    eqvar4: str
    #: Category for this Equipment, e.g. "Equipment", "Universal Equipment", "Battle Honour", etc.
    eqcategory: str