FROM python:3.8
ARG BUILDTYPE=production
ENV BUILDTYPE=${BUILDTYPE} \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    FLASK_APP=kailio.wsgi

MAINTAINER akail
LABEL description="Personal website and CMS system" \
      maintainer="Andrew <andrew@kail.io>"
EXPOSE 5000

RUN pip install poetry==1.0.0

COPY . /app

WORKDIR /app

RUN poetry install $(if [ "$BUILDTYPE" = 'production' ]; then echo '--no-dev'; fi) \
        -n --no-ansi \
        && if [ "$BUILDTYPE" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

VOLUME ["/app/kailio/static/uploads"]

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD run
