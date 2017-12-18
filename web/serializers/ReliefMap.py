from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import ReliefMap, Membership, MapItemTemplate, DataLayer

class ReliefMapSerializer(DynamicModelSerializer):
    mapItemTemplates = DynamicRelationField('web.serializers.MapItemTemplateSerializer',many=True, source='mapitemtemplate_set')
    dataLayers = DynamicRelationField('web.serializers.DataLayerSerializer',many=True, source='datalayer_set')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    def create(self, validated_data):
        reliefMap = ReliefMap.objects.create(**validated_data)

        user = self.context['request'].user
        Membership.objects.create(type='admin', memberable=reliefMap, user=user)

        templateData = {
            'reliefMap': reliefMap,
            'owner': user,
        }

        MapItemTemplate.objects.bulk_create([
            MapItemTemplate(name='Water Well', category='Resource', subCategory='Water, Sanitation, and Hygiene', **templateData),
            MapItemTemplate(name='Resevoir', category='Resource', subCategory='Water, Sanitation, and Hygiene', **templateData),
            MapItemTemplate(name='Water Main', category='Resource', subCategory='Water, Sanitation, and Hygiene', **templateData),
            MapItemTemplate(name='Water Purification Pill', category='Resource', subCategory='Water, Sanitation, and Hygiene', **templateData),
            MapItemTemplate(name='Evacuation Bus', category='Resource', subCategory='Logistics', **templateData),
            MapItemTemplate(name='ADRA Management Tent', category='Resource', subCategory='Logistics', **templateData),
            MapItemTemplate(name='Check In Tent', category='Resource', subCategory='Logistics', **templateData),
            MapItemTemplate(name='Malaria Kit', category='Resource', subCategory='Health', **templateData),
            MapItemTemplate(name='Vaccination Kit', category='Resource', subCategory='Health', **templateData),
            MapItemTemplate(name='Vitamins', category='Resource', subCategory='Nutrition', **templateData),
            MapItemTemplate(name='Evacuation Safe Zone', category='Resource', subCategory='Protection', **templateData),
            MapItemTemplate(name='Blanket', category='Resource', subCategory='Shelter', **templateData),
            MapItemTemplate(name='Refugee Camp', category='Resource', subCategory='Camp Coordination and Camp Management', **templateData),
            MapItemTemplate(name='Debris Dump', category='Resource', subCategory='Early Recovery', **templateData),
            MapItemTemplate(name='School', category='Resource', subCategory='Education', **templateData),
            MapItemTemplate(name='Food Rations', category='Resource', subCategory='Food & Security', **templateData),
            MapItemTemplate(name='Public Phone', category='Resource', subCategory='Emergency Telecommunications', **templateData),

            MapItemTemplate(name='Sinkhole', category='Hazard', **templateData),
            MapItemTemplate(name='Collapsed Powerline', category='Hazard', **templateData),
            MapItemTemplate(name='Gas leak', category='Hazard', **templateData),
            MapItemTemplate(name='Oil Spill', category='Hazard', **templateData),
            MapItemTemplate(name='Collapsed Road', category='Hazard', **templateData),
            MapItemTemplate(name='Blocked Road', category='Hazard', **templateData),
            MapItemTemplate(name='Flooded Area', category='Hazard', **templateData),
            MapItemTemplate(name='Unstable building', category='Hazard', **templateData),
            MapItemTemplate(name='Crack in the Road', category='Hazard', **templateData),
            MapItemTemplate(name='Burnt Area', category='Hazard', **templateData),
            MapItemTemplate(name='Fallen Tree', category='Hazard', **templateData),

            MapItemTemplate(name='Garbage Dump Zone', category='Community Involvement', **templateData),
            MapItemTemplate(name='Rally point', category='Community Involvement', **templateData),

            MapItemTemplate(name='Vegetable Garden', category='Other Resources', **templateData),
            MapItemTemplate(name='Swimming Pool', category='Other Resources', **templateData),
            MapItemTemplate(name='Room Available', category='Other Resources', **templateData),
            MapItemTemplate(name='Doctor', category='Other Resources', **templateData),
            MapItemTemplate(name='Dump Truck Driver', category='Other Resources', **templateData),
        ])

        return reliefMap


    class Meta:
        model = ReliefMap
        name = 'reliefMap'
        fields = ('id', 'name', 'description', 'mapItemTemplates', 'dataLayers', 'public', 'owner', 'createdAt', 'updatedAt')
