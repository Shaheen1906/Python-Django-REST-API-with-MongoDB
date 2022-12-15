from rest_framework import serializers 
from api.models import CRUD
from django.contrib.auth.models import User

 
 
class CRUDSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CRUD
        fields = ('id',
                  'User',
                  'name',
                  'img',
                  'summary')

class UserSerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(source="user.username",many=True, read_only=True)
    name = CRUDSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name']