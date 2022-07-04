FROM tiangolo/uvicorn-gunicorn:python3.9

RUN pip install --no-cache-dir fastapi

COPY ./app /app