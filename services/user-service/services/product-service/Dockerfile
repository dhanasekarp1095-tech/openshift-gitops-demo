FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

ENV APP_NAME=product-service
ENV APP_VERSION=v1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
