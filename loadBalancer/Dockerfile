FROM python:3.9

WORKDIR /applb

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8088", "app:app"]
