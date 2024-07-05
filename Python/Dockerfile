FROM python:3.8-slim

ARG ENV_VAR_NAME
ENV ENV_VAR_NAME=${ENV_VAR_NAME}

WORKDIR /app

COPY requirements.txt requirements.txt
COPY build_databases.py build_databases.py
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt


COPY . /app

CMD ["python", "build_databases.py", "app.py"]

