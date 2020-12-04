from datetime import datetime
from aoc_api.celery import app
from problems.services import AocApiException, ModelAutoCreateService
from problems.advent_service import AdventCreateService
from celery.schedules import crontab


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=1, hour=8), problem_uploader.s(datetime.year), name='uploader')


@app.task(autoretry_for=(AocApiException,), retry_backoff=True, retry_kwargs={'max_retries': 5}, default_retry_delay=30)
def problem_uploader(year):
    ModelAutoCreateService(AdventCreateService(year)())()
