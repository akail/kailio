FROM python:3.8
MAINTAINER akail

RUN git clone https://github.com/akail/kailio.git /app
WORKDIR /app

RUN pip install poetry==1.0.0
COPY poetry.lock pyproject.toml /app/

# Have to have the sed to filter out the -e of poetry.  That is because
# with the -e, pip doesn't install to the system site-packages, but instead in a
# src directory where the build occurs, and that can be wiped out if mounted over during development
RUN poetry config virtualenvs.create false \
    && poetry export --without-hashes -f requirements.txt \
    | sed 's/-e\ git/git/g' | pip install -r /dev/stdin

ENV FLASK_APP kailio.wsgi
# Should probably default to false

# TODO: AAK clone from git instead for production
VOLUME ["/app/kailio/static/uploads"]

EXPOSE 5000

LABEL description="Personal website and CMS system" \
      maintainer="Andrew <andrew@kail.io>"

ENTRYPOINT ["./boot.sh"]
CMD run
