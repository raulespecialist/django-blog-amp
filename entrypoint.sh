#!/bin/bash
#python core/manage.py migrate
python core/manage.py collectstatic --no-input --clear
#python core/manage.py compilemessages -f

export DJANGO_SETTINGS_MODULE=core.settings

exec gunicorn -c config/gunicorn/conf.py --bind :8000 --chdir core core.wsgi:application

exec "$@"