from web.models import MapItem

from django.db import models


class ReliefMap(models.Model):
    """
    A general relief map created by a user. Each map has many resources
    """

    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=1000, default="")

    owner = models.ForeignKey('auth.User', related_name='relief_maps', null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_map_items(self):
        return MapItem.objects.filter(relief_map=self)

    def __str__(self):
        return 'name: {0}, owner: {1}'.format(self.name, self.owner)