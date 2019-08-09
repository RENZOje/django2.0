from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.


class Clicker(models.Model):

    name =  models.TextField(max_length=50, unique=True)
    click = models.IntegerField(default=0)


    def __str__(self):
        return self.name