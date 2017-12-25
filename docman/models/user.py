from django.db import models

from docman.models import Role, Department
import bcrypt
import base64

# Create your models here.

class User(models.Model):
    firstname = models.CharField(blank=False, null=True, max_length=40)
    lastname = models.CharField(blank=False, null=True, max_length=40)
    username = models.CharField(blank=False, null=True, max_length=20)
    password = models.CharField(blank=False, null=False, max_length=255)
    email = models.CharField(blank=False, null=False, max_length=255)
    department = models.ForeignKey(Department)
    role = models.ForeignKey(Role)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True, blank=False, auto_now=True)

    def save(self):
        self.hash_password()
        super(User, self).save()
    
    def __str__(self):
        return self.firstname + " " + self.lastname

    def validate_password(self, password):
        return bcrypt.checkpw(base64.b64encode(password), str(self.password))

    def hash_password(self):
        self.password = bcrypt.hashpw(base64.b64encode(self.password), bcrypt.gensalt())