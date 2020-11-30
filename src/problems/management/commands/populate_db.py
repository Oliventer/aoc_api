from django.core.management.base import BaseCommand
from problems.services import ModelAutoCreateService


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        ModelAutoCreateService(2019)()
