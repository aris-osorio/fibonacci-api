release: python mensajes/manage.py makemigrations --no-input
release: python mensajes/manage.py migrate --no-input
release: python mensajes/manage.py collectstatic --noinput

web: gunicorn fibonacci2.wsgi:application --python fibonacci2 --log-file - --log-level debug 