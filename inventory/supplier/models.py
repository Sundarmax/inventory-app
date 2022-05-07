from statistics import mode
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name
