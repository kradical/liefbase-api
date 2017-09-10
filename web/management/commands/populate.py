from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from django.contrib.gis.geos import GEOSGeometry

from web.models import User, Organization, Membership, Team, MapItemTemplate, MapItem, ReliefMap

class Command(BaseCommand):
    help = "Populates a basic set of test data"

    def handle(self, *args, **options):
        user_data = {
            'username': 'test@liefbase.io',
            'password': 'password',
            'first_name': 'tester',
            'last_name': 'liefbase',
        }
        try:
            user = User.objects.get(username=user_data['username'])
            created = False
        except User.DoesNotExist:
            user = User.objects.create_user(**user_data)
            created = True
        print("Test User{} Created".format('' if created else ' Not'))
        print(user)
        print()        

        organization_data = {
            'name': 'Liefbase',
            'owner': user,
        }
        liefbase, created = Organization.objects.get_or_create(**organization_data)
        print("Test Organization{} Created".format('' if created else ' Not'))
        print(liefbase)
        print()

        membership_data = {
            'type': 'admin', 
            'memberable': liefbase, 
            'user': user,
        }
        membership, created = Membership.objects.get_or_create(**membership_data)
        print("Test Organization Admin{} Created".format('' if created else ' Not'))
        print(membership)
        print()

        map_data = {
            'name': 'TestMap',
            'description': 'Test description.',
            'owner': user,
        }
        relief_map, created = ReliefMap.objects.get_or_create(**map_data)
        print("Test Relief Map{} Created".format('' if created else ' Not'))
        print(relief_map)
        print()

        template_data = {
            'category': 'Resource',
            'relief_map': relief_map,
            'owner': user,
        }

        for name in ['Water Well', 'Resevoir', 'Water Main', 'Water Purification Pill', 'Soap', 'Toothbrush']:
            self.create_map_item_template(name=name, sub_category='Water, Sanitation, and Hygiene', **template_data)

        for name in ['Evacuation Bus', 'ADRA Management Tent', 'Check In Tent']:
            self.create_map_item_template(name=name, sub_category='Logistics', **template_data)

        for name in ['Malaria Kit', 'Vaccination Tent']:
            self.create_map_item_template(name=name, sub_category='Health', **template_data)

        for name in ['Vitamins']:
            self.create_map_item_template(name=name, sub_category='Nutrition', **template_data)

        for name in ['Evacuation Safe Zone', 'Missing Person Tent']:
            self.create_map_item_template(name=name, sub_category='Protection', **template_data)

        for name in ['Blanket', 'Mosquito Net']:
            self.create_map_item_template(name=name, sub_category='Shelter', **template_data)

        for name in ['Refugee Camp', 'Camp Washroom', 'Camp Showers']:
            self.create_map_item_template(name=name, sub_category='Camp Coordination and Camp Management', **template_data)

        for name in ['Debris Dump', 'Field Hospital']:
            self.create_map_item_template(name=name, sub_category='Early Recovery', **template_data)

        for name in ['School']:
            self.create_map_item_template(name=name, sub_category='Education', **template_data)

        for name in ['Food Rations', 'Community Farm']:
            self.create_map_item_template(name=name, sub_category='Food & Security', **template_data)

        for name in ['Wireless Tower', 'Public Phone']:
            resource_template = self.create_map_item_template(name=name, sub_category='Emergency Telecommunications', **template_data)

        template_data['category'] = 'Hazard'
        for name in ['Sinkhole', 'Collapsed Powerline', 'Gas leak', 'Oil Spill', 'Collapsed Road', 'Blocked Road', 'Flooded Area']:
            hazard_template = self.create_map_item_template(name=name, **template_data)

        map_item_data = {
            'quantity': 3,
            'owner': user,
            'template': resource_template,
        }

        lat = 48.4284210
        lng = -123.3656440

        for i in range(3):
            map_item_data['point'] = GEOSGeometry("POINT({} {})".format(lat + 0.01 * i, lng + 0.01 * i))
            self.create_map_item(**map_item_data)

        map_item_data['template'] = hazard_template
        for i in range(3):
            map_item_data['point'] = GEOSGeometry("POINT({} {})".format(lat - 0.01 * i, lng - 0.01 * i))
            self.create_map_item(**map_item_data)

    def create_map_item(self, **kwargs):
        map_item, created = MapItem.objects.get_or_create(**kwargs)
        print("Test Map Item{} Created".format('' if created else ' Not'))
        print(map_item)
        print()

    def create_map_item_template(self, **kwargs):
        template, created = MapItemTemplate.objects.get_or_create(**kwargs)

        print("Test Template{} Created".format('' if created else ' Not'))
        print(template)
        print()

        return template