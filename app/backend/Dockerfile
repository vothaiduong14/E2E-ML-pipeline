FROM python:3.8-slim
WORKDIR /app

# Install Java (JRE) in container since H2O uses Java
RUN apt-get update
RUN apt-get install -y default-jre

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]