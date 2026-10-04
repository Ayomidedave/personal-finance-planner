from datetime import date

from pydantic import BaseModel, Field


class BudgetCreate(BaseModel):
    category: str
    limit_amount: float = Field(gt=0)
    period: str


class BudgetResponse(BaseModel):
    id: int
    category: str
    limit_amount: float
    period: str

    model_config = {"from_attributes": True}


class SavingsGoalCreate(BaseModel):
    name: str
    target_amount: float = Field(gt=0)
    current_amount: float = Field(ge=0)
    deadline: date


class SavingsGoalResponse(BaseModel):
    id: int
    name: str
    target_amount: float
    current_amount: float
    deadline: date

    model_config = {"from_attributes": True}