from web.models import Team, Organization, User, Membership, ReliefMap

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.contenttypes.models import ContentType


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    username = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

class OrganizationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        org = Organization.objects.create(**validated_data)
        user = self.context['request'].user
        
        Membership.objects.create(type='admin', memberable=org, user=user)
        
        return org

    class Meta:
        model = Organization
        fields = ('id', 'name')

class TeamSerializer(serializers.ModelSerializer):
    parent_organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    
    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        user = self.context['request'].user

        Membership.objects.create(type='admin', memberable=team, user=user)

        return team

    class Meta:
        model = Team
        fields = ('id', 'name', 'parent_organization')
