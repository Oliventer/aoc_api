from bs4 import BeautifulSoup
import requests
from django.db import IntegrityError
from problems.models import Problem


class ModelAutoCreateService:
    def __init__(self, year):
        self.year = year

    def __call__(self):
        self.parse_problem()

    @staticmethod
    def _create_model(title, description, link):
        try:
            mdl = Problem(title=title, description=description, link=link)
            mdl.save()
            print(f'Task {title} successfully created!')
        except IntegrityError:
            print('Fail :^(')

    def get_all_days(self):
        days = []
        r = requests.get(f'https://adventofcode.com/{self.year}')

        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            if f'/{self.year}/day' in link.get('href'):
                days.append(link.get('href'))
        return days

    def parse_problem(self):
        days = self.get_all_days() # mock to /2019/day/25/
        for day in days:
            link = 'https://adventofcode.com'+day
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser').find('article')
            title = ''.join(soup.find('h2').contents)
            description = ''.join(soup.get_text()).replace(title, '')
            self._create_model(title, description, link)
