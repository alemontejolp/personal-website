# Personal Website

A website to introduce myself, show my public projects and my work experience.

Feel free to clone it and fill it with your information. ;)

This website was developed using Django (v4.2) [1] as web framework, Bootstrap (v5.3) [2] as frontend toolkit and Poetry (v1.5) [3] as dependency manager.

License: MIT

## Installation

### With Docker

#### Production

Build the image.

``` bash
docker build -t personal-website .
```

Create the container.

``` bash
docker create --name personal-website -e DATABASE_URL=postgresql://user:password@host.com/db -e SERVICE_HOSTNAME=my-hostname.com -p port_host:8000 personal-website
```

Start the container.

``` bash
docker start personal-website
```

See the logs (optional).

``` bash
docker logs personal-website --follow
```

Or use a docker-compose.yml

``` yml
# Filename: docker-compose.yml
version: "3.9"
services:
  mysite:
    build: .
    ports:
      - "port_host:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@host.com
      - SERVICE_HOSTNAME=my-hostname.com
```

And start the app with:

``` bash
docker compose up
```

Use the flag `-d` to detach the terminal.

#### Development

Build the image.

``` bash
docker build -t personal-website -f Dockerfile.dev .
```

Create the container.

``` bash
docker create --name personal-website -p 8080:8000 --volume .:/home/app personal-website
```

Start the container.

``` bash
docker start personal-website
```

See the logs (optional).

``` bash
docker logs personal-website --follow
```

Or use a docker-compose.dev.yml

``` yml
# Filename: docker-compose.dev.yml
version: "3.9"
services:
  mysite:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8080:8000"
    volumes:
      - .:/home/app
```

And start the app with:

``` bash
docker compose -f docker-compose.dev.yml up
```

### Without Docker
* Run `poetry install` to install the dependencies in a new virtual environment managed by Poetry.
* Run `poetry shell` to easy enter in a new shell with the virtual environment activated.
* Run `python manage.py migrate` to setup the database.
* Run `python manage.py runserver` to start the development server.

## Deployment

Settings for manual deployment on [Render](https://render.com/) are included [4]. See the deployment manual for Django apps.

`DEBUG` variable is set to true by default. But you can set it to false through the `DEBUG_MODE` environment variable set to `false`. It's automatically set to false when running on Render.

This project uses `DJ-Database-URL` to easily configure the database connection by a `DATABASE_URL` environment variable [5]. Just set that environment variable with a connection string for the project to use your desired database. If it's not set, the project uses the default `db.sqlite3` file as DB.

This project is intended to be used with a Postgres database on production, so the driver is listed in the dependencies. If you want to use other DBMS, you will need to install a proper driver. See the drivers that `DJ-Database-URL` supports [5]. If not supported, you will probably need to change the definition of the `DATABASES` configuration variable in `[project-dir]/website/settings.py`.

**IMPORTANT** If deploying natively on Render set the python and poetry version as described in the docs [4].

## Development

To make the environment variables management easier, the package `python-dotenv` is used [6]. So in your local environment (if not using Docker), you can place a `.env` file at the root of the project and set needed variables. This way you could have:

```
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

and connect with your development (or even production) database from your local environment, but you can always use the default sqlite db.

## References

1. [Django docs](https://docs.djangoproject.com/en/4.2/).
2. [Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
3. [Poetry docs](https://python-poetry.org/docs/).
4. [Docs for deploy Django projects on Render](https://render.com/docs/deploy-django).
5. [DJ-Database-URL docs](https://github.com/jazzband/dj-database-url#dj-database-url).
6. [Python Dotenv docs](https://pypi.org/project/python-dotenv/).
