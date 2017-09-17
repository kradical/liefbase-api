from web.models import MapItemTemplate, Memberable

from django.db import models

import json

class ReliefMap(Memberable):
    """
    A general relief map created by a user. Each map has many resources
    """

    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=1000, default="")
    public = models.BooleanField(default=False)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'templates': [x.to_dict() for x in self.mapitemtemplate_set.all()],
            'owner': self.owner.id,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

