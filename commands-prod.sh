#!/bin/bash
pdm install --prod
pdm run python manage.py collectstatic --noinput
pdm run python manage.py makemigrations --noinput
pdm run python manage.py migrate
pdm run python -m uvicorn src.framework.asgi:application --host 0.0.0.0 --port 8000