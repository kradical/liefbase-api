from web.models import MapItem
from web.serializers import MapItemSerializer
from web.permissions import ItemReliefMapPermission

from rest_framework import viewsets
from rest_framework.response import Response


class MapItemViewSet(viewsets.ModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = MapItemSerializer
    permission_classes = (ItemReliefMapPermission,)

    def update(self, request, pk=None):
        try:
            item = MapItem.objects.get(pk=pk)
        except MapItem.DoesNotExist:
            raise NotFound()

        try:
            coordinates = request.data["geometry"]["coordinates"]
            quantity = request.data['properties']['quantity']
        except KeyError:
            return Response({ 'detail': 'coordinates and quantity are required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        item.point.x = coordinates[0]
        item.point.y = coordinates[1]
        item.quantity = quantity

        item.save()

        serializer = MapItemSerializer(item)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        try:
            item = MapItem.objects.get(pk=pk)
        except MapItem.DoesNotExist:
            raise NotFound()

        try:
            coordinates = request.data["geometry"]["coordinates"]
            item.point.x = coordinates[0]
            item.point.y = coordinates[1]
        except KeyError:
            pass

        try:
            item.quantity = request.data['properties']['quantity']
        except KeyError:
            pass

        item.save()

        serializer = MapItemSerializer(item)
        return Response(serializer.data)
