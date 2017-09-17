from django.db import models

import json


class FilterPreset(models.Model):
    """
    A filter preset saved for a team or a user. Ex. A fireman wants to see his teams, the fires, and freshwater with one click
    """

    name = models.CharField(max_length=120)
    relief_map = models.ForeignKey('ReliefMap', on_delete=models.CASCADE)
    templates = models.ManyToManyField('MapItemTemplate')

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'relief_map': self.relief_map.id,
            'owner': self.owner.id,
            'templates': [x.id for x in self.templates.all()]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)
