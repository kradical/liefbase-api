from web.models import MapItemTemplate
from web.serializers import MapItemTemplateSerializer
from web.permissions import ObjectReliefMapPermission

from rest_framework import viewsets
from rest_framework.response import Response

class MapItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
    permission_classes = (ObjectReliefMapPermission,)

    def update(self, request, pk=None):
        try:
            template = MapItemTemplate.objects.get(pk=pk)
        except MapItemTemplate.DoesNotExist:
            raise NotFound()

        try:
            name, category, sub_category = (request.data[x] for x in ('name', 'category', 'sub_category'))
        except KeyError:
            return Response({ 'detail': 'name, category, sub_category are required fields'}, status=status.HTTP_400_BAD_REQUEST)

        template.name = name
        template.category = category
        template.sub_category = sub_category

        template.save()

        serializer = MapItemTemplateSerializer(template)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        try:
            template = MapItemTemplate.objects.get(pk=pk)
        except MapItemTemplate.DoesNotExist:
            raise NotFound()

        try:
            template.name = request.data['name']
        except KeyError:
            pass

        try:
            template.category = request.data['category']
        except KeyError:
            pass

        try:
            template.sub_category = request.data['sub_category']
        except KeyError:
            pass

        template.save()

        serializer = MapItemTemplateSerializer(template)
        return Response(serializer.data)
