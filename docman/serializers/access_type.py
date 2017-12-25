from rest_framework import serializers
from docman.models import AccessType

class AccessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessType
        fields = ('id', 'title', 'created', 'last_modified')
