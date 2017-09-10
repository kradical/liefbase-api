from django.db import models
from django.contrib.postgres.fields import JSONField

import json

class TemplatePreset(models.Model):
    """
    A preset of templates that are selected when a relief map is created.
    """

    name = models.CharField(max_length=120)
    raw_templates = JSONField()

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'raw_templates': self.raw_templates,
            'owner': self.owner.id,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)


