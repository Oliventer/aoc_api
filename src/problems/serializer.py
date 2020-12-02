from rest_framework import serializers
from problems.models import Problem, Advent


class AdventSerializer(serializers.ModelSerializer):

    link = serializers.SerializerMethodField()

    class Meta:
        model = Advent
        fields = ['year', 'link']

    def get_link(self, obj):
        return self.context["request"].build_absolute_uri(f'/advents/{obj.pk}/problems/')


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'title', 'description', 'advent', 'link', 'day', ]
