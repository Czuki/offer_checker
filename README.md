# offer_checker

`python3 -m venv venv`

`pip3 install requirements.txt`

`python3 manage.py migrate`

REDIS
`docker run -d -p 6379:6379 redis`

CELERY
`celery -A offer_checker worker -l INFO`

CELERY BEAT
`celery -A offer_checker beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
