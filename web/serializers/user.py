from web.models import ReliefMap

from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    relief_maps = serializers.PrimaryKeyRelatedField(many=True, queryset=ReliefMap.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'relief_maps')