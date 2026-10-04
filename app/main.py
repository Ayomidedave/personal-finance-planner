from fastapi import FastAPI

from app.database import Base, engine
from app.planning import models as planning_models
from app.transactions import models as transaction_models
from app.transactions.router import router as transactions_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Finance Planner",
    description="A personal finance and budgeting application.",
    version="0.1.0",
)

app.include_router(transactions_router)


@app.get("/")
def root():
    return {"message": "Personal Finance Planner API is running"}