from datetime import date

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    type: str
    category: str
    description: str
    date: date


class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    description: str
    date: date

    model_config = {"from_attributes": True}