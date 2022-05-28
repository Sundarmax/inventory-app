import imp
from operator import mod
from statistics import mode
from unicodedata import category
from django.db import models
from django.utils import timezone
from supplier.models import Supplier

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=40)
    product_description = models.CharField(max_length=40,blank=True,null=True)
    product_unit = models.CharField(max_length=40,null=True,blank=True)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_status = models.IntegerField()
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_supplier = models.ManyToManyField(Supplier,related_name="product_supplier_map",blank=True)


    def __str__(self):
        return self.product_name
    class Meta:
        ordering = ['-id']


def get_all_suppliers():
    suppliers = Product.objects.prefetch_related("product_supplier")

    for sup in suppliers:
        print(sup.product_supplier.all())
