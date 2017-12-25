from rest_framework import serializers
from docman.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'content', 'owner', 'accessType', 'documentType', 'created', 'last_modified')