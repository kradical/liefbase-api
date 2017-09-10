from django.db import models

import json

class MapItemTemplate(models.Model):
    """
    A template created by an organization. Ex. Blanket, Bucket of Water, Oil Spill
    """

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120, default='Other')
    sub_category = models.CharField(max_length=120, default='Other')
    relief_map = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'sub_category': self.sub_category,
            'relief_map': self.relief_map.id,
            'map_items': [x.to_dict() for x in self.mapitem_set.all()],
            'owner': self.owner.id,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

