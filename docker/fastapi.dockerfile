FROM python:3.11

ENV SQLALCHEMY_DATABASE_URL "postgresql://postgres:postgres@postgres:5432/postgres"

# COPY . /tmp/

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]