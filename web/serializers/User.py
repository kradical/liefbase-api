from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from web.models import Team, Organization, User, Membership, ReliefMap

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    firstName = serializers.CharField(required=False, source='first_name')
    lastName = serializers.CharField(required=False, source='last_name')
    createdAt = serializers.DateTimeField(read_only=True, source='date_joined')
    lastLogin = serializers.DateTimeField(read_only=True, source='last_login')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'firstName', 'lastName', 'password', 'createdAt', 'lastLogin')

class OrganizationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        org = Organization.objects.create(owner=user, **validated_data)

        Membership.objects.create(type='admin', memberable=org, user=user)

        return org

    class Meta:
        model = Organization
        fields = ('id', 'name', 'owner', 'createdAt', 'updatedAt')

class TeamSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), source='parent')

    def create(self, validated_data):
        user = self.context['request'].user
        team = Team.objects.create(owner=user, **validated_data)

        Membership.objects.create(type='admin', memberable=team, user=user)

        return team

    class Meta:
        model = Team
        fields = ('id', 'name', 'organization', 'owner', 'createdAt', 'updatedAt')

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id', 'type', 'memberable', 'user', 'createdAt', 'updatedAt')
