FROM myweb:0.2

ARG CURRNT_ENV=prod

WORKDIR /dist
COPY poetry.log pyproject.toml /dist/

RUN poetry config settings.virtualenvs.creat false \
    && poetry install $(test "$CURRNT_ENV" == prod && echo '--no-dev') --no-interaction --no-ansi

COPY . /dist

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]