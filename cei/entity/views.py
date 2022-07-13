from rest_framework import viewsets

from . import models, serializers


class EntityViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post")
    queryset = models.Entity.objects.all().order_by("-created_at")
    serializer_class = serializers.EntitySerializer
