FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry export --without-hashes -f requirements.txt --dev \
    | pip install -r /dev/stdin

ENV FLASK_APP kailio.wsgi
# Should probably default to false
ENV FLASK_DEBUG True

COPY . /app/

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
