from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import engine, SessionLocal, Base
from models import User, Transaction
from schemas import TransactionCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transaction Reward System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def calculate_score(total_amount, total_transactions):
    return (total_amount * 0.1) + (total_transactions * 20)


@app.get("/")
def home():
    return {"message": "API Running Successfully"}


@app.post("/transaction")
def create_transaction(transaction: TransactionCreate):

    db: Session = SessionLocal()

    try:

        existing_transaction = db.query(Transaction).filter(
            Transaction.transaction_id == transaction.transactionId
        ).first()

        if existing_transaction:
            raise HTTPException(
                status_code=400,
                detail="Duplicate transaction ID"
            )

        new_transaction = Transaction(
            transaction_id=transaction.transactionId,
            user_id=transaction.userId,
            amount=transaction.amount
        )

        db.add(new_transaction)

        user = db.query(User).filter(
            User.user_id == transaction.userId
        ).first()

        if not user:

            user = User(
                user_id=transaction.userId,
                total_amount=0,
                total_transactions=0,
                score=0
            )

            db.add(user)

        user.total_amount += transaction.amount
        user.total_transactions += 1

        user.score = calculate_score(
            user.total_amount,
            user.total_transactions
        )

        db.commit()

        return {
            "message": "Transaction Added Successfully"
        }

    finally:
        db.close()


@app.get("/summary/{user_id}")
def get_summary(user_id: str):

    db: Session = SessionLocal()

    try:

        user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "userId": user.user_id,
            "totalAmount": user.total_amount,
            "totalTransactions": user.total_transactions,
            "score": user.score
        }

    finally:
        db.close()


@app.get("/ranking")
def get_ranking():

    db: Session = SessionLocal()

    try:

        users = db.query(User).order_by(
            User.score.desc()
        ).all()

        rankings = []

        for index, user in enumerate(users, start=1):

            rankings.append({
                "rank": index,
                "userId": user.user_id,
                "score": user.score,
                "totalAmount": user.total_amount,
                "totalTransactions": user.total_transactions
            })

        return rankings

    finally:
        db.close()
