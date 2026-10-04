from datetime import date
from fastapi.testclient import TestClient
from app.main import app

from app.database import Base, SessionLocal, engine
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate
from app.transactions.service import (
    calculate_balance,
    calculate_total_expenses,
    calculate_total_income,
    create_transaction,
    get_transactions,
)


def test_calculate_total_income():
    transactions = [
        Transaction(
            amount=2000,
            type="income",
            category="Salary",
            description="Monthly salary",
            date=date(2026, 10, 1),
        ),
        Transaction(
            amount=500,
            type="income",
            category="Freelance",
            description="Freelance work",
            date=date(2026, 10, 2),
        ),
    ]

    assert calculate_total_income(transactions) == 2500


def test_calculate_total_expenses():
    transactions = [
        Transaction(
            amount=300,
            type="expense",
            category="Food",
            description="Groceries",
            date=date(2026, 10, 2),
        ),
        Transaction(
            amount=200,
            type="expense",
            category="Transport",
            description="Metro",
            date=date(2026, 10, 3),
        ),
    ]

    assert calculate_total_expenses(transactions) == 500


def test_calculate_balance():
    transactions = [
        Transaction(
            amount=2000,
            type="income",
            category="Salary",
            description="Monthly salary",
            date=date(2026, 10, 1),
        ),
        Transaction(
            amount=500,
            type="expense",
            category="Food",
            description="Groceries",
            date=date(2026, 10, 2),
        ),
    ]

    assert calculate_balance(transactions) == 1500



def test_create_and_get_transaction():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    try:
        transaction_data = TransactionCreate(
            amount=2500,
            type="income",
            category="Salary",
            description="Monthly salary",
            date=date(2026, 10, 1),
        )

        created = create_transaction(db, transaction_data)

        assert created.amount == 2500
        assert created.type == "income"

        transactions = get_transactions(db)

        assert any(transaction.id == created.id for transaction in transactions)
    finally:
        db.close()


def test_transaction_api():
    client = TestClient(app)

    response = client.post(
        "/transactions/",
        json={
            "amount": 100,
            "type": "expense",
            "category": "Food",
            "description": "Lunch",
            "date": "2026-10-04",
        },
    )

    assert response.status_code == 200
    assert response.json()["amount"] == 100

    response = client.get("/transactions/")

    assert response.status_code == 200
    assert len(response.json()) > 0