from problems.models import Advent


class AdventCreateService:
    def __init__(self, year):
        self.year = year

    def __call__(self, *args, **kwargs):
        return self._get_existing_model() or self._create_model()

    def _create_model(self):
        advent = Advent(year=self.year)
        advent.save()
        return advent

    def _get_existing_model(self):
        try:
            obj = Advent.objects.get(pk=self.year)
            return obj
        except Advent.DoesNotExist:
            return None
