from datetime import date
from fastapi.testclient import TestClient
from app.main import app

from app.database import SessionLocal
from app.planning.models import Budget, SavingsGoal
from app.planning.schemas import BudgetCreate, SavingsGoalCreate
from app.planning.service import (
    calculate_budget_remaining,
    calculate_savings_progress,
    calculate_savings_remaining,
    create_budget,
    create_savings_goal,
    get_budgets,
    get_savings_goals,
    is_budget_exceeded,
    is_savings_goal_completed,
)

def test_budget_remaining():
    budget = Budget(
        category="Food",
        limit_amount=500,
        period="monthly",
    )

    assert calculate_budget_remaining(budget, 350) == 150


def test_budget_exceeded():
    budget = Budget(
        category="Food",
        limit_amount=500,
        period="monthly",
    )

    assert is_budget_exceeded(budget, 600) is True
    assert is_budget_exceeded(budget, 400) is False


def test_savings_progress():
    goal = SavingsGoal(
        name="New Laptop",
        target_amount=2000,
        current_amount=500,
        deadline=date(2027, 6, 1),
    )

    assert calculate_savings_progress(goal) == 25


def test_savings_remaining():
    goal = SavingsGoal(
        name="New Laptop",
        target_amount=2000,
        current_amount=500,
        deadline=date(2027, 6, 1),
    )

    assert calculate_savings_remaining(goal) == 1500


def test_savings_remaining_never_negative():
    goal = SavingsGoal(
        name="New Laptop",
        target_amount=2000,
        current_amount=2200,
        deadline=date(2027, 6, 1),
    )

    assert calculate_savings_remaining(goal) == 0


def test_savings_goal_completed():
    goal = SavingsGoal(
        name="New Laptop",
        target_amount=2000,
        current_amount=2000,
        deadline=date(2027, 6, 1),
    )

    assert is_savings_goal_completed(goal) is True


def test_savings_goal_not_completed():
    goal = SavingsGoal(
        name="New Laptop",
        target_amount=2000,
        current_amount=1500,
        deadline=date(2027, 6, 1),
    )

    assert is_savings_goal_completed(goal) is False



def test_create_and_get_budget():
    db = SessionLocal()

    try:
        budget_data = BudgetCreate(
            category="Transport",
            limit_amount=300,
            period="monthly",
        )

        created = create_budget(db, budget_data)

        assert created.category == "Transport"
        assert created.limit_amount == 300

        budgets = get_budgets(db)

        assert any(budget.id == created.id for budget in budgets)
    finally:
        db.close()


def test_create_and_get_savings_goal():
    db = SessionLocal()

    try:
        goal_data = SavingsGoalCreate(
            name="Emergency Fund",
            target_amount=5000,
            current_amount=1000,
            deadline=date(2027, 12, 31),
        )

        created = create_savings_goal(db, goal_data)

        assert created.name == "Emergency Fund"
        assert created.target_amount == 5000

        goals = get_savings_goals(db)

        assert any(goal.id == created.id for goal in goals)
    finally:
        db.close()

def test_planning_api():
    client = TestClient(app)

    response = client.post(
        "/planning/budgets",
        json={
            "category": "Entertainment",
            "limit_amount": 200,
            "period": "monthly",
        },
    )

    assert response.status_code == 200
    assert response.json()["category"] == "Entertainment"

    response = client.post(
        "/planning/savings-goals",
        json={
            "name": "New Phone",
            "target_amount": 1000,
            "current_amount": 250,
            "deadline": "2027-01-01",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "New Phone"

    response = client.get("/planning/budgets")
    assert response.status_code == 200

    response = client.get("/planning/savings-goals")
    assert response.status_code == 200