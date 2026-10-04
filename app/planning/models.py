from datetime import date

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    limit_amount: Mapped[float] = mapped_column(Float, nullable=False)
    period: Mapped[str] = mapped_column(String(20), nullable=False)


class SavingsGoal(Base):
    __tablename__ = "savings_goals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    target_amount: Mapped[float] = mapped_column(Float, nullable=False)
    current_amount: Mapped[float] = mapped_column(Float, nullable=False)
    deadline: Mapped[date] = mapped_column(Date, nullable=False)