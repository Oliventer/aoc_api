from django.db import models


class Advent(models.Model):
    year = models.IntegerField(primary_key=True, unique=True)


class Problem(models.Model):
    title = models.TextField()
    description = models.TextField()
    link = models.CharField(unique=True, blank=False, max_length=256)
    day = models.IntegerField()
    advent = models.ForeignKey(Advent, on_delete=models.CASCADE)

    class Meta:
        ordering = ['day']
        unique_together = ('day', 'advent')
