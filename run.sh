#!/bin/bash

LOG_DIR='.'
ERROR_LOG="${LOG_DIR}/error.log"
ACCESS_LOG="${LOG_DIR}/access.log"
gunicorn pymaze.wsgi:application \
	--name pymaze \
	--bind 0.0.0.0:8000 \
	--workers 3 \
	--log-level=info \
	--log-file=${ERROR_LOG} \
	--access-logfile=${ACCESS_LOG} \
	"$@"
