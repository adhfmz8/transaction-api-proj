from fastapi import FastAPI, Response, Depends
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from models import Transaction
from db import init_db, get_session


@asynccontextmanager
async def lifespan(applet: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/v1/transaction")
async def get_all_transactions(
    session: Session = Depends(get_session),
) -> list[Transaction]:
    transactions = session.exec(select(Transaction)).all()
    return list(transactions)


@app.post("/api/v1/transaction")
async def post_transaction(
    t: Transaction, session: Session = Depends(get_session)
) -> Transaction:
    transaction = Transaction(name=t.name, cost=t.cost, frequency=t.frequency)

    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction
