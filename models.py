from pydantic import BaseModel


class Link(BaseModel):
    file: str
