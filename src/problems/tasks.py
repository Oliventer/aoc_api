from datetime import datetime
from aoc_api.celery import app
from problems.services import ModelAutoCreateService
from problems.advent_service import AdventCreateService
from celery.schedules import crontab


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=1, hour=8), problem_uploader.s(), name='uploader')


@app.task
def problem_uploader():
    ModelAutoCreateService(AdventCreateService(datetime.year)())()
