# Use the official Python image
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY src/ /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]