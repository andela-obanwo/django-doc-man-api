from rest_framework import serializers
from docman.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'title', 'created', 'last_modified')

