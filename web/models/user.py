from django.contrib.auth.models import AbstractUser
from django.db import models

import json

class User(AbstractUser):
    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

class Memberable(models.Model):
    def cast(self):
        """
        Converts "self" into its correct child class
        """
        for name in dir(self):
            try:
                attr = getattr(self, name)
                if isinstance(attr, self.__class__):
                    return attr
            except:
                pass
        
        return self

    def get_instance_name(self):
        for name in dir(self):
            try:
                attr = getattr(self, name)
                if isinstance(attr, self.__class__):
                    return name
            except:
                pass
        
        return 'Memberable'

class Organization(Memberable):
    name = models.CharField(max_length=100, unique=True)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner.id,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

class Team(Memberable):
    name = models.CharField(max_length=100, null=False, blank=False)
    parent_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False)

    owner = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner.id,
            'parent_organization': self.parent_organization.id,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

class Membership(models.Model):
    MEMBERSHIP_TYPES = (
        ('admin', 'admin'),
        ('member', 'member'),
    )

    type = models.CharField(max_length=32, choices=MEMBERSHIP_TYPES, null=False, blank=False)
    memberable = models.ForeignKey(Memberable, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'memberable_type': self.memberable.get_instance_name(),
            'memberable': self.memberable.cast().to_dict(),
            'user': self.user.to_dict(),
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)

