from pydantic import BaseModel


class Link(BaseModel):
    filename: str
    link: str
