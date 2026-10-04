from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.planning import service
from app.planning.schemas import (
    BudgetCreate,
    BudgetResponse,
    SavingsGoalCreate,
    SavingsGoalResponse,
)

router = APIRouter(
    prefix="/planning",
    tags=["Planning"],
)

DbSession = Annotated[Session, Depends(get_db)]


@router.post("/budgets", response_model=BudgetResponse)
def create_budget(
    budget_data: BudgetCreate,
    db: DbSession,
):
    return service.create_budget(db, budget_data)


@router.get("/budgets", response_model=list[BudgetResponse])
def get_budgets(db: DbSession):
    return service.get_budgets(db)


@router.post("/savings-goals", response_model=SavingsGoalResponse)
def create_savings_goal(
    goal_data: SavingsGoalCreate,
    db: DbSession,
):
    return service.create_savings_goal(db, goal_data)


@router.get("/savings-goals", response_model=list[SavingsGoalResponse])
def get_savings_goals(db: DbSession):
    return service.get_savings_goals(db)