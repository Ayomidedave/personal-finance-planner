from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.transactions import service
from app.transactions.schemas import TransactionCreate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=TransactionResponse)
def create_transaction(
    transaction_data: TransactionCreate,
    db: DbSession,
):
    return service.create_transaction(db, transaction_data)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: DbSession):
    return service.get_transactions(db)