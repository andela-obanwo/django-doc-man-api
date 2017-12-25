from django.db import models

class DocumentType(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True, blank=False, auto_now=True)

    
    def __str__(self):
        return self.title