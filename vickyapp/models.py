from django.db import models

# Create your models here.
class vickytest(models.Model):
    firstname = models.CharField(max_length=10,null=True, blank=True, default=False)
    lastname = models.CharField(max_length=10,null=True, blank=True, default=False)
    email = models.CharField(max_length=20,null=True, blank=True, default=False)
    saction = models.IntegerField(null=True, blank=True, default=False)