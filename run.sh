#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

LOG_DIR='.'
ERROR_LOG="${LOG_DIR}/error.log"
ACCESS_LOG="${LOG_DIR}/access.log"

touch ${ERROR_LOG}
touch ${ACCESS_LOG}
tail -n 0 -f ${ERROR_LOG} &

gunicorn pymaze.wsgi:application \
	--name pymaze \
	--bind 0.0.0.0:8000 \
	--workers 3 \
	--log-level=info \
	--log-file=${ERROR_LOG} \
	--access-logfile=${ACCESS_LOG} \
	"$@"
