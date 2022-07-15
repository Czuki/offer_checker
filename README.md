# offer_checker

REDIS
`docker run -d -p 6379:6379 redis`

CELERY
`celery -A offer_checker worker -l INFO -P gevent`

CELERY BEAT
`celery -A offer_checker beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`

SELENIUM HUB
`java -jar selenium-server-4.1.2.jar hub`

SELENIUM NODE
`java -jar selenium-server-4.1.2.jar node`