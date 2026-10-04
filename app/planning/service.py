from sqlalchemy.orm import Session

from app.planning.models import Budget, SavingsGoal
from app.planning.schemas import BudgetCreate, SavingsGoalCreate


def create_budget(
    db: Session,
    budget_data: BudgetCreate,
) -> Budget:
    budget = Budget(
        category=budget_data.category,
        limit_amount=budget_data.limit_amount,
        period=budget_data.period,
    )

    db.add(budget)
    db.commit()
    db.refresh(budget)

    return budget


def get_budgets(db: Session) -> list[Budget]:
    return db.query(Budget).all()


def create_savings_goal(
    db: Session,
    goal_data: SavingsGoalCreate,
) -> SavingsGoal:
    goal = SavingsGoal(
        name=goal_data.name,
        target_amount=goal_data.target_amount,
        current_amount=goal_data.current_amount,
        deadline=goal_data.deadline,
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal


def get_savings_goals(db: Session) -> list[SavingsGoal]:
    return db.query(SavingsGoal).all()

def calculate_budget_remaining(
    budget: Budget,
    spending: float,
) -> float:
    return budget.limit_amount - spending

def is_budget_exceeded(
    budget: Budget,
    spending: float,
) -> bool:
    return spending > budget.limit_amount

def calculate_savings_progress(goal: SavingsGoal) -> float:
    return (goal.current_amount / goal.target_amount) * 100

def calculate_savings_remaining(goal: SavingsGoal) -> float:
    return max(goal.target_amount - goal.current_amount, 0)

def is_savings_goal_completed(goal: SavingsGoal) -> bool:
    return goal.current_amount >= goal.target_amount