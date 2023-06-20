FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY services services
COPY app.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
