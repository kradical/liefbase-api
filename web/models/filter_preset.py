from django.conf import settings
from django.db import models


class FilterPreset(models.Model):
    """
    A filter preset saved for a team or a user. Ex. A fireman wants to see his teams, the fires, and freshwater with one click
    """

    name = models.CharField(max_length=120)
    relief_map = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)
    templates = models.ManyToManyField('MapItemTemplate')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'name: {0}, relief map: {1}'.format(self.name, self.relief_map)
