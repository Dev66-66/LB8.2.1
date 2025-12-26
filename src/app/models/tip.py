from pydantic import BaseModel

class Tip(BaseModel):
    id: int = None
    text: str