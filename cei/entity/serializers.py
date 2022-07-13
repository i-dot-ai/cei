from rest_framework import serializers

from . import models


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Entity
        fields = ['id', 'created_at']
