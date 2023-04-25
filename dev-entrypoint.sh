#!/bin/bash

set -e
set -o nounset

# Load environment variables from .env file
if [ -f ./.env ]; then
  source ./.env
else
  echo "No .env file found. Exiting."
  exit 1
fi

redis_ready() {
    python << END
import sys

from redis import Redis
from redis import RedisError


try:
    redis = Redis.from_url("${CELERY_URL_BROKER}", db=0)
    redis.ping()
except RedisError:
    sys.exit(-1)
END
}


wait_other_containers() {
	until redis_ready; do
		>&2 echo "Waiting for Redis to become available..."
		sleep 5
	done
	>&2 echo "Redis is available"
}

django_operations() {
	python3 manage.py collectstatic --noinput
	python3 manage.py migrate
}

cd /app


case $1 in
	"bash")
		bash;;
	"makemigrations")
		python3 manage.py makemigrations;;
	"worker")
		wait_other_containers ;\
		django_operations ;\
		celery \
		--app myshop \
			worker \
			--loglevel INFO
		;;
	"server")
		wait_other_containers ;\
		django_operations ;\
		wait_other_containers ;\
		python manage.py runserver 0.0.0.0:8000
				;;
	"createsuperuser")
		wait_other_containers ;\
		django_operations ;\
		python manage.py createsuperuser
		;;
	"shell")
		wait_other_containers ;\
		django_operations ;\
		python manage.py shell
		;;
	"test")
		wait_other_containers ;\
		django_operations ;\
		pytest
		;;
	"lint")
		isort --check-only myshop tests
		black --check myshop tests
		flake8 myshop tests
		mypy myshop
		;;
	"*")
		exec "$@"
		;;
esac

