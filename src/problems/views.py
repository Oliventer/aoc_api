from rest_framework import viewsets, mixins, status
from problems.models import Problem, Advent
from problems.serializer import ProblemSerializer, AdventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Max
from django.forms.models import model_to_dict


class AdventViewset(viewsets.ModelViewSet):
    queryset = Advent.objects.all()
    serializer_class = AdventSerializer


class ProblemViewset(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_queryset(self):
        return Problem.objects.filter(advent=self.kwargs['advent_pk'])

    @action(detail=False, methods=["GET"])
    def last(self, request, *args, **kwargs):
        problem = self.get_queryset().order_by('day').last()
        serializer = self.get_serializer(problem)
        return Response(serializer.data)
