from django.contrib import admin
from django.urls import path,include
from api import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('op/', views.CRUDList.as_view()),
    path('op/<int:pk>/',views.CRUDDetail.as_view()),
    

]