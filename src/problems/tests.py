import pytest
from rest_framework.test import APIClient
from freezegun import freeze_time
from problems.models import Problem
from problems.services import ModelAutoCreateService


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def model_instance(api):
    api.post('/problems/', {'title': 'TestTitle', 'description': 'Fon-Zon', 'link': 'TestLink'})


@pytest.fixture
def mocked_get_all_days(mocker):
    mocker.patch('problems.services.ModelAutoCreateService.get_all_days',
                 return_value=['/2019/day/24'])


def test_model_instance_creation(api, model_instance):
    assert Problem.objects.last().description == 'Fon-Zon'


def test_every_model_url_are_unique(api, model_instance):
    r = api.post('/problems/', {'title': 'Test', 'description': 'Not Fon-Zon', 'link': 'TestLink'})
    assert r.status_code == 400
    assert Problem.objects.last().description == 'Fon-Zon'


def test_service_object_create_model_instance(api, mocked_get_all_days):
    ModelAutoCreateService(2019)()
    assert Problem.objects.last().link == 'https://adventofcode.com/2019/day/24'
