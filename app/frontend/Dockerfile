# syntax=docker/dockerfile:1
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4200

CMD ["streamlit", "run", "main.py"]