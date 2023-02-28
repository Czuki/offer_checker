#!/bin/bash

case $1 in

  env)
    /bin/bash -c ". venv/bin/activate; exec /bin/bash --norc -i"
    ;;

  build_env)
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    playwright install
    ;;

  run_redis)
    docker run -d -p 6379:6379 redis
    ;;

  run_celery_beat)
    celery -A offer_checker beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ;;

  run_celery)
    celery -A offer_checker worker -l INFO
    ;;

  run)
    source venv/bin/activate
    python3 manage.py runserver
    ;;

  *)
    echo 'Available options:'
    echo 'run                - Run Django app'
    echo 'build_env          - Creates virtual environment and installs all requirements'
    echo 'run_redis          - Use docker to run redis on default port 6379'
    echo 'run_celery         - Run celery'
    echo 'run_celery_beat    - Run celery scheduler'
    ;;
esac
