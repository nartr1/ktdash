from pydantic import BaseModel

class TacOp(BaseModel):
    tacopid: str
    archetype: str
    tacopseq: int
    title: str
    description: str