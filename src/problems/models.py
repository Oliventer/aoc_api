from django.db import models


class Problem(models.Model):
    title = models.TextField()
    description = models.TextField()
    link = models.CharField(unique=True, blank=False, max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
