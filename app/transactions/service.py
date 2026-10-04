from sqlalchemy.orm import Session

from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate


def create_transaction(
    db: Session,
    transaction_data: TransactionCreate,
) -> Transaction:
    transaction = Transaction(
        amount=transaction_data.amount,
        type=transaction_data.type,
        category=transaction_data.category,
        description=transaction_data.description,
        date=transaction_data.date,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


def get_transactions(db: Session) -> list[Transaction]:
    return db.query(Transaction).order_by(Transaction.date.desc()).all()


def calculate_total_income(transactions: list[Transaction]) -> float:
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.type == "income"
    )


def calculate_total_expenses(transactions: list[Transaction]) -> float:
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.type == "expense"
    )


def calculate_balance(transactions: list[Transaction]) -> float:
    return calculate_total_income(transactions) - calculate_total_expenses(
        transactions
    )