from offer_checker.celery import app


@app.task(bind=True)
def debug_task(self):
    print('bazinga')
    print(f'Request: {self.request!r}')
