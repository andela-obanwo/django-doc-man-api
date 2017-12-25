from django.db import models

class AccessType(models.Model):
    title = models.CharField(blank=False, null=False, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True, blank=False, auto_now=True)

    
    def __str__(self):
        return self.title