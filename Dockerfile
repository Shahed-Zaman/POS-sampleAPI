FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./src /app
COPY requirements.txt /apps/requirements.txt
RUN pip install -r /apps/requirements.txt
ENV PYTHONPATH=${PYTHONPATH}:/apps/src
