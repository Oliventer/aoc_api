from django.core.management.base import BaseCommand
from problems.services import ModelAutoCreateService
from problems.advent_service import AdventCreateService


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        ModelAutoCreateService(AdventCreateService(2019)())()
