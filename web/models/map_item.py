from django.conf import settings
from django.contrib.gis.db import models


class MapItem(models.Model):
    """
    A map item instance. Defined by its template, is specific to one map.
    """

    quantity = models.FloatField()
    point = models.PointField()
    relief_map = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)
    template = models.ForeignKey('MapItemTemplate', on_delete=models.CASCADE)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'quantity: {0}, point: {1}, relief_map: {2}, template: {3}'.format(self.quantity, self.point, self.relief_map.id, self.template.id)
