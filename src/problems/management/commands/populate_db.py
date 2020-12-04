from django.core.management.base import BaseCommand
from problems.tasks import problem_uploader


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        problem_uploader.delay(2019)
