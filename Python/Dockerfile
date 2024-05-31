FROM python:3.8-slim

ARG ENV_VAR_NAME
ENV ENV_VAR_NAME=${ENV_VAR_NAME}

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
