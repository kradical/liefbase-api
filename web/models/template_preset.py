from django.conf import settings
from django.db import models


class TemplatePreset(models.Model):
    """
    A preset of templates that are created automatically when a relief map is created.
    """

    name = models.CharField(max_length=120)
    raw_templates = model.CharField(max_length=1000)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'name: {0}, raw templates: {1}'.format(self.name, self.raw_templates)
