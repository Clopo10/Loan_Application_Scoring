import logging
import os

# Make directory data for logs (if it doesn't exist)
os.makedirs("../data", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("../data/api_logs.txt"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("loan_application_api")