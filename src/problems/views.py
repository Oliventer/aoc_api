from rest_framework import viewsets, mixins, status
from problems.models import Problem, Advent
from problems.serializer import ProblemSerializer, AdventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class AdventViewset(viewsets.ModelViewSet):
    queryset = Advent.objects.all()
    serializer_class = AdventSerializer


class ProblemViewset(viewsets.ModelViewSet):
    serializer_class = ProblemSerializer
    lookup_field = 'day'

    def get_queryset(self):
        return Problem.objects.filter(advent=self.kwargs['advent_pk'])

    @action(detail=False, methods=["GET"])
    def last(self, request, *args, **kwargs):
        problem = self.get_queryset().order_by('day').last()
        serializer = self.get_serializer(problem)
        return Response(serializer.data)
