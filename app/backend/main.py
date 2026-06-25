from fastapi import FastAPI
from schemas import LoanApplication
import score_eval
from logger import logger

app = FastAPI(title="Loan Application Scoring API")

logger.info("Loan Application API started successfully.")

@app.post("/predict")
def evaluate_loan_application(application: LoanApplication):
    # Log the incoming request data
    logger.info(f"Evaluating loan: Amount= ${application.loan_amount}, Age= {application.age}, Income= ${application.income}, Credit Score= {application.credit_score}")

    # Calculate the risk score using the score_eval module
    risk_score = score_eval.calculate_risk_score(application)

    # Determine the risk category and log the result
    if risk_score <= 30:
        risk_category = "HIGH"
        logger.info(f"Application denied. Risk Score: {round(risk_score, 2)}\n---------------------------------------------------------------------------------------------")
        
    elif 30 < risk_score < 70:
        risk_category = "MEDIUM"
        logger.info(f"Application flagged for manual review. Risk Score: {round(risk_score, 2)}\n---------------------------------------------------------------------------------------------")
        
    else:
        risk_category = "LOW"
        logger.info(f"Application approved. Risk Score: {round(risk_score, 2)}\n---------------------------------------------------------------------------------------------")
        

    return {
        "risk_score": round(risk_score, 2),
        "risk_category": risk_category
    }