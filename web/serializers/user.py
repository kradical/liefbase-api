from web.models import Team, Organization, User, Membership, ReliefMap

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.contenttypes.models import ContentType


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

class OrganizationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.create(owner=user, **validated_data)
        
        Membership.objects.create(type='admin', memberable=org, user=user)
        
        return org

    class Meta:
        model = Organization
        fields = ('id', 'name')

class TeamSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        team = Team.objects.create(owner=user, **validated_data)

        Membership.objects.create(type='admin', memberable=team, user=user)

        return team

    class Meta:
        model = Team
        fields = ('id', 'name', 'parent_organization')

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id', 'type', 'memberable', 'user')
