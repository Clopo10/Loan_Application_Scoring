from pydantic import BaseModel

class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int