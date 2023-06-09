FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install "poetry==1.5"
RUN poetry config virtualenvs.create false
RUN poetry install

CMD exec gunicorn -c "./gunicorn/gunicorn.conf.py" -k "uvicorn.workers.UvicornWorker" \
    "src.bootstrap.main:bootstrap(['properties:./properties/properties.ini','secrets:./secrets/secrets.ini'])"
