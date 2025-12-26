from pydantic import BaseModel

class Quote(BaseModel):
    id: int = None
    text: str
    author: str