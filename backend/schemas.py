from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    userId: str
    amount: float = Field(gt=0)
    transactionId: str


class UserSummary(BaseModel):
    userId: str
    totalAmount: float
    totalTransactions: int
    score: float
