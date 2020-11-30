from rest_framework import viewsets
from problems.models import Problem
from problems.serializer import ProblemSerializer


class ProblemViewset(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
