from django.contrib.contenttypes.models import ContentType

from rest_framework.serializers import CharField, DateTimeField, CurrentUserDefault, SerializerMethodField
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import Team, Organization, User, Membership, Memberable

class UserSerializer(DynamicModelSerializer):
    password = CharField(required=True, write_only=True)
    firstName = CharField(required=False, source='first_name')
    lastName = CharField(required=False, source='last_name')
    createdAt = DateTimeField(read_only=True, source='date_joined')
    lastLogin = DateTimeField(read_only=True, source='last_login')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        name = 'user'
        fields = ('id', 'username', 'firstName', 'lastName', 'password', 'createdAt', 'lastLogin')

class OrganizationSerializer(DynamicModelSerializer):
    owner = DynamicRelationField('UserSerializer', read_only=True, default=CurrentUserDefault())

    def create(self, validated_data):
        org = Organization.objects.create(**validated_data)
        membership = Membership.objects.create(type='admin', memberable=org, user=org.owner)

        membership.memberable.get_instance_name()
        return org

    class Meta:
        model = Organization
        name = 'organization'
        fields = ('id', 'name', 'owner', 'createdAt', 'updatedAt')

class TeamSerializer(DynamicModelSerializer):
    organization = DynamicRelationField('OrganizationSerializer', source='parent')
    owner = DynamicRelationField('UserSerializer', read_only=True, default=CurrentUserDefault())

    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        Membership.objects.create(type='admin', memberable=team, user=team.owner)
        return team

    class Meta:
        model = Team
        name = 'team'
        fields = ('id', 'name', 'organization', 'owner', 'createdAt', 'updatedAt')

class MembershipSerializer(DynamicModelSerializer):
    user = DynamicRelationField('UserSerializer')
    memberable = DynamicRelationField('MemberableSerializer')
    memberableType = SerializerMethodField()

    def get_memberableType(self, obj):
        name = obj.memberable.get_instance_name()
        return name

    class Meta:
        model = Membership
        fields = ('id', 'type', 'memberable', 'memberableType', 'user', 'createdAt', 'updatedAt')

class MemberableSerializer(DynamicModelSerializer):
    def to_representation(self, instance):
        name = instance.get_instance_name()

        data = None
        if name == 'reliefmap':
            from web.serializers import ReliefMapSerializer
            data = ReliefMapSerializer().to_representation(instance.cast())
        elif name == 'organization':
            data = OrganizationSerializer().to_representation(instance.cast())
        elif name == 'team':
            data = TeamSerializer().to_representation(instance.cast())

        return data

    class Meta:
        model = Memberable
        fields = '__all__'

