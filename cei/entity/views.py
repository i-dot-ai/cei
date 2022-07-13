from rest_framework import viewsets

from . import models, serializers


class EntityViewSet(viewsets.ModelViewSet):
    queryset = models.Entity.objects.all().order_by('-created_at')
    serializer_class = serializers.EntitySerializer
