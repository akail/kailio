FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/

# Have to have the sed to filter out the -e of poetry.  That is because
# with the -e, pip doesn't install to the system site-packages, but instead in a 
# src directory where the build occurs, and that can be wiped out if mounted over during development
RUN poetry config virtualenvs.create false \
    && poetry export --without-hashes -f requirements.txt --dev \
    | sed 's/-e\ git/git/g' | pip install -r /dev/stdin

ENV FLASK_APP kailio.wsgi
# Should probably default to false
ENV FLASK_DEBUG True

COPY . /app/

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
