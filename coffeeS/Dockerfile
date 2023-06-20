FROM python:3.9

ARG APP_PORT=8080

WORKDIR /app

ENV ENV_PORT=$APP_PORT

COPY requirements.txt .
COPY services services
COPY app.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python -m gunicorn --bind 0.0.0.0:$ENV_PORT app:app
