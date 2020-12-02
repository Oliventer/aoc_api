from bs4 import BeautifulSoup
import requests
from django.db import IntegrityError
from problems.models import Problem, Advent


class ModelAutoCreateService:
    def __init__(self, advent):
        self.advent = advent

    def __call__(self):
        self.parse_all_problems()

    def _create_model(self, title, description, link, day):
        mdl = Problem(title=title, description=description, day=day, advent=self.advent, link=link)
        try:
            mdl.save()
        except IntegrityError:
            print('Fail :^(')
        else:
            print(f'Task {title} successfully created!')

    def get_all_days(self):
        r = requests.get(f'https://adventofcode.com/{self.advent.year}')

        soup = BeautifulSoup(r.text, 'html.parser')
        days = filter(lambda link: f'/{self.advent.year}/day/25' in link,
                      map(lambda a: a.get('href'), reversed(soup.find_all('a'))))
        return days

    def parse_all_problems(self):
        for day in self.get_all_days():
            link = 'https://adventofcode.com' + day

    def parse_problem(self, link):
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser').find('article')
        title = ''.join(soup.find('h2').contents)
        description = ''.join(soup.get_text()[1:])
        day = int(link.rstrip('/').split('/')[-1])
        self._create_model(title, description, link, day)
