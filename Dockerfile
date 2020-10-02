FROM python:3.8 AS build
RUN pip install poetry==1.0.0


ADD https://api.github.com/repos/akail/kailio/compare/master...HEAD /dev/null
RUN git clone --depth 1 https://github.com/akail/kailio.git /app
WORKDIR /app

RUN poetry config virtualenvs.in-project true && poetry install

# main build
FROM python:3.8 AS production
COPY --from=build /app /app

ENV FLASK_APP kailio.wsgi
MAINTAINER akail
LABEL description="Personal website and CMS system" \
      maintainer="Andrew <andrew@kail.io>"
EXPOSE 5000

# old
# Should probably default to false

# TODO: AAK clone from git instead for production



# This add ensures the latest revision has been pulled

#COPY poetry.lock pyproject.toml /app/

# Have to have the sed to filter out the -e of poetry.  That is because
# with the -e, pip doesn't install to the system site-packages, but instead in a
# src directory where the build occurs, and that can be wiped out if mounted over during development
#RUN poetry config virtualenvs.create false \
    #&& poetry export --without-hashes -f requirements.txt -o requirements.txt && cat requirements.txt \
    #| sed 's/-e\ git/git/g' | pip install -r /dev/stdin

VOLUME ["/app/kailio/static/uploads"]

ENTRYPOINT ["./boot.sh"]
CMD run
