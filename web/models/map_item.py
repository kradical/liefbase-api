from django.contrib.gis.db import models

import json


class MapItem(models.Model):
    """
    A map item instance. Defined by its template, is specific to one map.
    """

    quantity = models.FloatField()
    point = models.PointField()
    template = models.ForeignKey('MapItemTemplate', on_delete=models.CASCADE)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'type': 'Feature',
            'properties': {
                'quantity': self.quantity,
                'template': self.template.id,
                'owner': self.owner.id,
            },
            'point': {
                'type': 'Point',
                'coordinates': [self.point.x, self.point.y]
            },
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

