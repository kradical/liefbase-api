from django.contrib.auth import models as authModels
from django.db import models
from django.conf import settings

class User(authModels.User):
    pass

class Memberable(models.Model):
    pass

class Organization(Memberable):
    name = models.CharField(max_length=100, unique=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Team(Memberable):
    name = models.CharField(max_length=100, null=False, blank=False)
    parent_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Membership(models.Model):
    MEMBERSHIP_TYPES = (
        ('admin', 'admin'),
        ('member', 'member'),
    )

    type = models.CharField(max_length=32, choices=MEMBERSHIP_TYPES, null=False, blank=False)
    memberable = models.ForeignKey(Memberable, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

