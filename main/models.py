from django.db import models


class Database(models.Model):
    tm = models.DateTimeField(auto_now_add=False, blank=False)
    account = models.CharField(max_length=100, blank=False)
    symbol = models.CharField(max_length=100, blank=False)
    position = models.FloatField(null=False, blank=False)

# Create your models here.
