from rest_framework import serializers
from docman.models import DocumentType

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('id', 'title', 'created', 'last_modified')
