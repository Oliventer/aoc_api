import pytest
from rest_framework.test import APIClient
from freezegun import freeze_time
from problems.models import Problem, Advent
from problems.services import ModelAutoCreateService
from problems.advent_service import AdventCreateService
from django.db import IntegrityError


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def advent():
    advent = Advent(year=100500)
    advent.save()
    return advent


@pytest.fixture
def problem(advent):
    problem = Problem(title='TestTitle', description='Fon-Zon', advent=advent, link='TestLink', day=100500)
    problem.save()
    return problem


@pytest.fixture
def mocked_get_all_days(mocker):
    mocker.patch('problems.services.ModelAutoCreateService.get_all_days',
                 return_value=['/2019/day/24'])


@pytest.fixture
def mocked_parse_problem(mocker):
    def fake_parse(self, link):
        link = 'https://adventofcode.com/2019/day/100500'
        title = 'TestTitle'
        description = 'Mocked mock'
        day = 25
        self._create_model(title, description, link, day)
    mocker.patch('problems.services.ModelAutoCreateService.parse_problem', fake_parse)


def test_every_problem_url_is_unique(advent, problem):
    with pytest.raises(IntegrityError, match='UNIQUE'):
        problem = Problem(title='TestTitle', description='Fon-Zon-Reborn', advent=advent, link='TestLink', day=100500)
        problem.save()


def test_problem_service_objects_creation(mocked_get_all_days, mocked_parse_problem):
    ModelAutoCreateService(AdventCreateService(2019)())()
    assert Problem.objects.last().link == 'https://adventofcode.com/2019/day/100500'


def test_advent_service_objects_creation():
    AdventCreateService(100500)()
    assert Advent.objects.last().year == 100500


def test_nested_relationship(api, problem):
    response = api.get('/advents/100500/problems/1/')
    assert response.status_code == 200


def test_last_endpoint(api, problem, advent):
    problem = Problem(title='TestTitle', description='Fon-Zon-Reborn', advent=advent, link='TestLink2', day=100499)
    problem.save()
    response = api.get('/advents/100500/problems/last/')
    assert response.data['day'] == 100500
