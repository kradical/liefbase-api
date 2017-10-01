import json

from django.db import models

class MapItemTemplate(models.Model):
    """
    A template created by an organization. Ex. Blanket, Bucket of Water, Oil Spill
    """

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120, default='Other')
    subCategory = models.CharField(max_length=120, default='Other')
    reliefMap = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'subCategory': self.subCategory,
            'reliefMap': self.reliefMap.id,
            'mapItems': [x.to_dict() for x in self.mapitem_set.all()],
            'owner': self.owner.id,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat(),
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

