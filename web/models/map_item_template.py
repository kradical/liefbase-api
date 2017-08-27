from django.db import models


class MapItemTemplate(models.Model):
    """
    A template created by an organization. Ex. Blanket, Bucket of Water, Oil Spill
    """

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120, default='Other')
    sub_category = models.CharField(max_length=120, default='Other')

    def __str__(self):
        return 'name: {0}, category: {1}, sub_category: {2}'.format(self.name, self.category, self.sub_category)
