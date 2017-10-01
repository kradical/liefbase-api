import json

from django.contrib.gis.db import models

class MapItem(models.Model):
    """
    A map item instance. Defined by its mapItemTemplate, is specific to one map.
    """

    quantity = models.FloatField()
    point = models.PointField()
    mapItemTemplate = models.ForeignKey('MapItemTemplate', on_delete=models.CASCADE)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'type': 'Feature',
            'properties': {
                'quantity': self.quantity,
                'mapItemTemplate': self.mapItemTemplate.id,
                'owner': self.owner.id,
                'createdAt': self.createdAt.isoformat(),
                'updatedAt': self.updatedAt.isoformat(),
            },
            'point': {
                'type': 'Point',
                'coordinates': [self.point.x, self.point.y]
            },
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

