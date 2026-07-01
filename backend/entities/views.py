from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Entity
from .serializers import EntitySerializer

class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def get_queryset(self):
        queryset = Entity.objects.all()
        country = self.request.query_params.get('country')
        entity_type = self.request.query_params.get('entity_type')

        if country:
            queryset = queryset.filter(country=country)
        if entity_type:
            queryset = queryset.filter(entity_type=entity_type)

        return queryset