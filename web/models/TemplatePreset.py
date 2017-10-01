import json

from django.contrib.postgres.fields import JSONField
from django.db import models

class TemplatePreset(models.Model):
    """
    A preset of templates that are selected when a relief map is created.
    """

    name = models.CharField(max_length=120)
    rawTemplates = JSONField()

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rawTemplates': self.rawTemplates,
            'owner': self.owner.id,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat(),
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)


