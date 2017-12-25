from rest_framework import serializers
from docman.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'email', 'username', 'role', 'created', 'last_modified')
