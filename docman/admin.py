from django.contrib import admin
from models import User, Role, Document, DocumentType, AccessType, Department
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Document)
admin.site.register(DocumentType)
admin.site.register(AccessType)
admin.site.register(Department)
