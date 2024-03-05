from pydantic import BaseModel


class Transaction(BaseModel):
    value: int
    type: str
    description: str
