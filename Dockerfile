FROM python:3.9

ARG CURRNT_ENV=prod

ENV POETRY_VERSION=1.1.12

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -
 
WORKDIR /dist
COPY poetry.log pyproject.toml /dist/

RUN poetry config settings.virtualenvs.creat false \
    && poetry install $(test "$CURRNT_ENV" == prod && echo '--no-dev') --no-interaction --no-ansi

COPY . /dist

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]