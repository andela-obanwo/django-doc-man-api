from rest_framework import serializers
from docman.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'created', 'last_modified')
