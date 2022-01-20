FROM myweb:0.2

ARG CURRNT_ENV=prod

WORKDIR /dist
COPY poetry.lock pyproject.toml /dist/

RUN export PATH="/root/.local/bin:$PATH" \
    && poetry config settings.virtualenvs.creat false \
    && poetry install $(test "$CURRNT_ENV" == prod && echo '--no-dev') --no-interaction --no-ansi

COPY . /dist

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]