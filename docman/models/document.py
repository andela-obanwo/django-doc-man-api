from django.db import models

from docman.models import User, DocumentType, AccessType

class Document(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    content = models.TextField(null=True)
    access_type = models.ForeignKey(AccessType)
    document_type = models.ForeignKey(DocumentType)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True, blank=False, auto_now=True)

    
    def __str__(self):
        return self.title