from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from django.contrib.gis.geos import GEOSGeometry

from meteor.models import User, UserAccountManager, Organization, ReliefMap, HazardTemplate, ResourceTemplate, HazardInstance, ResourceInstance

class Command(BaseCommand):
    help = "Populates a basic set of test data"

    def handle(self, *args, **options):
        try:
            liefbase = Organization.objects.get(name="Liefbase")
        except Organization.DoesNotExist:
            liefbase = Organization(name="Liefbase")
            liefbase.save()
            print("Created ", end='')

        print("Test Organization")
        print(liefbase.to_dict())
        print()

        try:
            user = User.objects.get(email='test@test.test')
        except User.DoesNotExist:
            user = UserAccountManager().create_user(first_name='test', last_name='test', org_id=liefbase.id, email='test@test.test', password='testpassword')
            print("Created ", end='')

        print("Test User")
        print(user.to_dict())
        print("password: testpassword")
        print()

        try:
            relief_map = ReliefMap.objects.get(name='TestMap')
        except ReliefMap.DoesNotExist:
            relief_map = ReliefMap(name='TestMap', description='This is a test relief map.', created_by=user)
            relief_map.save()
            print("Created ", end='')

        print("Test ReliefMap")
        print(relief_map.to_dict())
        print()

        for name in ['Sinkhole', 'Collapsed Powerline', 'Gas leak', 'Oil Spill', 'Collapsed Road', 'Blocked Road', 'Flooded Area']:
            try:
                hazard_template = HazardTemplate.objects.get(name=name, relief_map=relief_map)
            except HazardTemplate.DoesNotExist:
                hazard_template = HazardTemplate(name=name, relief_map=relief_map)
                hazard_template.save()
                print("Created ", end='')

            print("Test HazardTemplate")
            print(hazard_template.to_dict())
            print()

        for name in ['Water Well', 'Resevoir', 'Water Main', 'Water Purification Pill', 'Soap', 'Toothbrush']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Water, Sanitation, and Hygiene', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Evacuation Bus', 'ADRA Management Tent', 'Check In Tent']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Logistics', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Malaria Kit', 'Vaccination Tent']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Health', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Vitamins']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Nutrition', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()


        for name in ['Evacuation Safe Zone', 'Missing Person Tent']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Protection', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Blanket', 'Mosquito Net']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Shelter', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()


        for name in ['Refugee Camp', 'Camp Washroom', 'Camp Showers']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Camp Coordination and Camp Management', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Debris Dump', 'Field Hospital']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Early Recovery', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['School']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Education', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Food Rations', 'Community Farm']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Food & Security', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        for name in ['Wireless Tower', 'Public Phone']:
            try:
                resource_template = ResourceTemplate.objects.get(name=name, relief_map=relief_map)
            except ResourceTemplate.DoesNotExist:
                resource_template = ResourceTemplate(name=name, category='Emergency Telecommunications', relief_map=relief_map)
                resource_template.save()
                print("Created ", end='')

            print("Test ResourceTemplate")
            print(resource_template.to_dict())
            print()

        if len(HazardInstance.objects.filter(relief_map=relief_map)) >= 3:
            for hazard in HazardInstance.objects.filter(relief_map=relief_map):
                print("Test HazardInstance")
                print(hazard.to_dict())
                print()

        lat = 48.4284210
        lng = -123.3656440
        while len(HazardInstance.objects.filter(relief_map=relief_map)) < 3:
            geocoords = GEOSGeometry("POINT(%(lat)f %(lng)f)" % locals())
            hazard = HazardInstance(location=geocoords, relief_map=relief_map, template=hazard_template)
            hazard.save()

            print("Created Test HazardInstance")
            print(hazard.to_dict())
            print()

            lat += 0.01
            lng += 0.01

        if len(ResourceInstance.objects.filter(relief_map=relief_map)) >= 3:
            for resource in ResourceInstance.objects.filter(relief_map=relief_map):
                print("Test ResourceInstance")
                print(resource.to_dict())
                print()

        while len(ResourceInstance.objects.filter(relief_map=relief_map)) < 3:
            geocoords = GEOSGeometry("POINT(%(lat)f %(lng)f)" % locals())
            resource = ResourceInstance(location=geocoords, quantity=1, relief_map=relief_map, template=resource_template)
            resource.save()

            print("Created Test ResourceInstance")
            print(resource.to_dict())
            print()

            lat += 0.01
            lng += 0.01
