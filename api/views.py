from rest_framework import generics
from api import serializer
from django.contrib.auth.models import User
from api.models import *
from rest_framework import permissions



# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

class CRUDList(generics.ListCreateAPIView):
    queryset = CRUD.objects.all()
    serializer_class = serializer.CRUDSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CRUDDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CRUD.objects.all()
    serializer_class = serializer.CRUDSerializer
    permission_classes = [permissions.IsAuthenticated]