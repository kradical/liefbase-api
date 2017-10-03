from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from django.contrib.gis.geos import GEOSGeometry

from web.models import User, Organization, Membership, Team, MapItemTemplate, MapItem, ReliefMap, FilterPreset, TemplatePreset

class Command(BaseCommand):
    help = "Populates a basic set of test data"

    def handle(self, *args, **options):
        userData = {
            'username': 'test@liefbase.io',
            'password': 'password',
            'first_name': 'tester',
            'last_name': 'liefbase',
        }
        try:
            user = User.objects.get(username=userData['username'])
            created = False
        except User.DoesNotExist:
            user = User.objects.create_user(**userData)
            created = True
        print("Test User{} Created".format('' if created else ' Not'))
        print(user)
        print()

        organizationData = {
            'name': 'Liefbase',
            'owner': user,
        }
        try:
            liefbase = Organization.objects.get(name=organizationData['name'])
            created = False
        except Organization.DoesNotExist:
            liefbase = Organization.objects.create(**organizationData)
            created = True
        print("Test Organization{} Created".format('' if created else ' Not'))
        print(liefbase)
        print()

        membershipData = {
            'type': 'admin',
            'memberable': liefbase,
            'user': user,
        }
        membership, created = Membership.objects.get_or_create(**membershipData)
        print("Test Organization Admin{} Created".format('' if created else ' Not'))
        print(membership)
        print()

        mapData = {
            'name': 'TestMap',
            'description': 'Test description.',
            'owner': user,
        }
        reliefMap, created = ReliefMap.objects.get_or_create(**mapData)
        print("Test Relief Map{} Created".format('' if created else ' Not'))
        print(reliefMap)
        print()

        templateData = {
            'category': 'Resource',
            'reliefMap': reliefMap,
            'owner': user,
        }

        for name in ['Water Well', 'Resevoir', 'Water Main', 'Water Purification Pill', 'Soap', 'Toothbrush']:
            self.create_map_item_template(name=name, subCategory='Water, Sanitation, and Hygiene', **templateData)

        for name in ['Evacuation Bus', 'ADRA Management Tent', 'Check In Tent']:
            self.create_map_item_template(name=name, subCategory='Logistics', **templateData)

        for name in ['Malaria Kit', 'Vaccination Tent']:
            self.create_map_item_template(name=name, subCategory='Health', **templateData)

        for name in ['Vitamins']:
            self.create_map_item_template(name=name, subCategory='Nutrition', **templateData)

        for name in ['Evacuation Safe Zone', 'Missing Person Tent']:
            self.create_map_item_template(name=name, subCategory='Protection', **templateData)

        for name in ['Blanket', 'Mosquito Net']:
            self.create_map_item_template(name=name, subCategory='Shelter', **templateData)

        for name in ['Refugee Camp', 'Camp Washroom', 'Camp Showers']:
            self.create_map_item_template(name=name, subCategory='Camp Coordination and Camp Management', **templateData)

        for name in ['Debris Dump', 'Field Hospital']:
            self.create_map_item_template(name=name, subCategory='Early Recovery', **templateData)

        for name in ['School']:
            self.create_map_item_template(name=name, subCategory='Education', **templateData)

        for name in ['Food Rations', 'Community Farm']:
            self.create_map_item_template(name=name, subCategory='Food & Security', **templateData)

        for name in ['Wireless Tower', 'Public Phone']:
            resourceTemplate = self.create_map_item_template(name=name, subCategory='Emergency Telecommunications', **templateData)

        templateData['category'] = 'Hazard'
        for name in ['Sinkhole', 'Collapsed Powerline', 'Gas leak', 'Oil Spill', 'Collapsed Road', 'Blocked Road', 'Flooded Area']:
            hazardTemplate = self.create_map_item_template(name=name, **templateData)

        mapItemData = {
            'quantity': 3,
            'owner': user,
            'mapItemTemplate': resourceTemplate,
        }

        lat = 48.4284210
        lng = -123.3656440

        for i in range(3):
            mapItemData['point'] = GEOSGeometry("POINT({} {})".format(lat + 0.01 * i, lng + 0.01 * i))
            self.create_map_item(**mapItemData)

        mapItemData['mapItemTemplate'] = hazardTemplate
        for i in range(3):
            mapItemData['point'] = GEOSGeometry("POINT({} {})".format(lat - 0.01 * i, lng - 0.01 * i))
            self.create_map_item(**mapItemData)

        self.create_filter_preset(reliefMap=reliefMap, owner=user)

        self.create_template_preset(reliefMap=reliefMap, owner=user)

    def create_filter_preset(self, reliefMap, owner):
        mapItemTemplates = MapItemTemplate.objects.filter(reliefMap=reliefMap)[:5]
        filterPreset, created = FilterPreset.objects.get_or_create(name="Random Filter", reliefMap=reliefMap, owner=owner)
        print("Test Filter Preset{} Created".format('' if created else ' Not'))
        if created:
            print("Test Filter Preset Created")
            for template in mapItemTemplates:
                filterPreset.mapItemTemplates.add(template)
                print("Test Template {} added to Filter Preset".format(template))
        else:
            print("Test Filter Preset Not Created")
        print(filterPreset)
        print()

    def create_template_preset(self, reliefMap, owner):
        mapItemTemplates = MapItemTemplate.objects.filter(reliefMap=reliefMap)[:5]
        templatesJson = []
        for template in mapItemTemplates:
            templatesJson.append({
                'name': template.name,
                'category': template.category,
                'subCategory': template.subCategory
            })
        templatePreset, created = TemplatePreset.objects.get_or_create(name="Random Templates", owner=owner, rawTemplates=templatesJson)
        print("Test Template Preset{} Created".format('' if created else ' Not'))
        print(templatePreset)
        print()

    def create_map_item(self, **kwargs):
        mapItem, created = MapItem.objects.get_or_create(**kwargs)
        print("Test Map Item{} Created".format('' if created else ' Not'))
        print(mapItem)
        print()

    def create_map_item_template(self, **kwargs):
        mapItemTemplate, created = MapItemTemplate.objects.get_or_create(**kwargs)
        print("Test Template{} Created".format('' if created else ' Not'))
        print(mapItemTemplate)
        print()

        return mapItemTemplate
