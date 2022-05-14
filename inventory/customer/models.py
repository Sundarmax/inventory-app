from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id =models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=120,null=True,blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name
