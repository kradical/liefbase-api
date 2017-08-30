from web.models import Group, User, Membership, ReliefMap

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
    type = serializers.HiddenField(default='organization')
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Group.objects.filter(type='organization'))],   
    )

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)
        current_user = self.context['request'].user
        
        Membership.objects.create(type='admin', memberable=group, user=current_user)
        
        return group

    class Meta:
        model = Group
        fields = ('id', 'name', 'type')
