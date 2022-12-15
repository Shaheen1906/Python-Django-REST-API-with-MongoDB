from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CRUD)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','User','name','img','summary']