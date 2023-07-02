FROM python:3.10.12-alpine

ENV HOME_APP=/home/app

ENV DEBUG_MODE=false

RUN mkdir -p $HOME_APP

WORKDIR $HOME_APP

COPY . .

RUN pip install poetry==1.5.1

RUN poetry config virtualenvs.in-project true

RUN poetry install

RUN mkdir -p staticfiles

RUN poetry run python3 manage.py collectstatic --no-input

# RUN poetry run python3 manage.py migrate

EXPOSE 8000

CMD cat ./start.sh | sh
