from django.db import models

# Create your models here.
class CRUD(models.Model):
    User =  models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=False,)
    img = models.URLField()
    summary = models.CharField(max_length=500, blank=False,)