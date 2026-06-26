# 1. Start with a lightweight Python computer
FROM python:3.11-slim

# 2. Create the working folder inside the container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 5. Expose the port
EXPOSE 8000

# 6. Turn Uvicorn on, allowing outside traffic (0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]