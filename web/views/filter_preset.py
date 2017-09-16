from web.models import FilterPreset, MapItemTemplate, ReliefMap
from web.serializers import FilterPresetSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class FilterPresetViewSet(viewsets.ModelViewSet):
    queryset = FilterPreset.objects.all()
    serializer_class = FilterPresetSerializer

    def create(self, request):
        try:
            name, relief_map_id, templates = (request.data[x] for x in ('name', 'relief_map', 'templates'))
        except KeyError:
            return Response({ 'detail': 'name, templates are required fields'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            relief_map = ReliefMap.objects.get(pk=relief_map_id)
        except ReliefMap.DoesNotExist:
            raise NotFound()

        filter_preset = FilterPreset.objects.create(relief_map=relief_map, name=name)
        filter_preset.save()

        for template_id in templates:
            try:
                template = MapItemTemplate.objects.get(pk=template_id)
                filter_preset.templates.add(template)
            except MapItemTemplate.DoesNotExist:
                raise NotFound()

        serializer = FilterPresetSerializer(filter_preset)
        return Response(serializer.data)
