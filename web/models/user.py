from django.contrib.auth import models
from django.db.models import Model, IntegerField, CharField, ForeignKey, CASCADE
from django.conf import settings

class User(models.User):
    pass

class Memberable(Model):
    pass

class Group(Memberable):
    GROUP_TYPES = (
        ('organization', 'organization'),
        ('team', 'team'),
    )

    name = CharField(max_length=100, null=False, blank=False)
    type = CharField(max_length=32, choices=GROUP_TYPES, null=False, blank=False)
    parent = ForeignKey('Group', on_delete=CASCADE, null=True, default=None)

class Membership(Model):
    MEMBERSHIP_TYPES = (
        ('admin', 'admin'),
        ('member', 'member'),
    )

    type = CharField(max_length=32, choices=MEMBERSHIP_TYPES, null=False, blank=False)
    memberable = ForeignKey(Memberable, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

