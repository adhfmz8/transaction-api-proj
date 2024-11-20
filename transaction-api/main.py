from typing import Type, Sequence

from fastapi import FastAPI, Response, Depends, HTTPException
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from models import Transaction, EditTransaction
from db import init_db, get_session


@asynccontextmanager
async def lifespan(applet: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/v1/transaction")
async def get_all_transactions(
    session: Session = Depends(get_session),
) -> Sequence[Transaction]:
    transactions = session.exec(select(Transaction)).all()
    return transactions


@app.post("/api/v1/transaction")
async def post_transaction(
    t: Transaction, session: Session = Depends(get_session)
) -> Transaction:
    transaction = Transaction(name=t.name, cost=t.cost)

    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction


@app.get("/api/v1/transaction/{id_num}")
async def get_transaction(id_num: int, session: Session = Depends(get_session)):

    transaction = session.get(Transaction, id_num)

    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction with id {id_num} not found")

    return transaction


@app.put("/api/v1/transaction/{id_num}")
async def update_transaction(
        t: EditTransaction,
        id_num: int,
        session: Session = Depends(get_session)
):

    transaction: Type[Transaction] = session.get(Transaction, id_num)

    if not transaction:
        raise HTTPException(status_code=404, detail=f"Transaction with id {id_num} not found")

    if t.name is not None:
        transaction.name = t.name
    if t.cost is not None:
        transaction.cost = t.cost

    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction
