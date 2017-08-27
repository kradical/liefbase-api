from web.models import ReliefMap

from rest_framework import serializers

from django.contrib.auth.models import User


class ReliefMapSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReliefMap
        fields = ('id', 'name', 'description', 'owner')

class UserSerializer(serializers.ModelSerializer):
    relief_maps = serializers.PrimaryKeyRelatedField(many=True, queryset=ReliefMap.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'relief_maps')