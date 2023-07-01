poetry run python3 manage.py migrate
poetry run gunicorn -b 0.0.0.0:8000 --workers=4 --worker-tmp-dir /dev/shm --threads=4 --worker-class=gthread website.wsgi:application
