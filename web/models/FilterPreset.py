import json

from django.db import models

class FilterPreset(models.Model):
    """
    A filter preset saved for a team or a user. Ex. A fireman wants to see his teams, the fires, and freshwater with one click
    """

    name = models.CharField(max_length=120)
    reliefMap = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)
    mapItemTemplates = models.ManyToManyField('MapItemTemplate')

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'reliefMap': self.reliefMap.id,
            'mapItemTemplates': [x.id for x in self.mapItemTemplates.all()],
            'owner': self.owner.id,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat(),
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)
