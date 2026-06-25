from schemas import LoanApplication

def calculate_risk_score(loan_application: LoanApplication) -> float:
    """
    Calculate the risk score for a loan application based on the applicant's age, income, loan amount, and credit score.

    Args:
        loan_application (LoanApplication): The loan application data.

    Returns:
        float: The calculated risk score.
    """

    # Normalize the input values (0 - 100)

    # 18 = 0; 60+ = 100
    norm_age = max(0, min(100, ((loan_application.age - 18) / 42) * 100))
    # 100,000+ = 100
    norm_income = max(0, min(100, (loan_application.income / 100000) * 100))
    # 50,000 = 0; 0 = 100
    norm_loan_amount = max(0, min(100, 100 - ((loan_application.loan_amount / 50000) * 100)))
    # 300 = 0; 850 = 100
    norm_credit_score = max(0, min(100, ((loan_application.credit_score - 300) / 550) * 100))

    # Assign weights to each factor
    weight_age = 0.1
    weight_income = 0.3
    weight_loan_amount = 0.2
    weight_credit_score = 0.4

    # Calculate and return the risk score
    return ((norm_age * weight_age) + (norm_income * weight_income) + (norm_loan_amount * weight_loan_amount) + (norm_credit_score * weight_credit_score))