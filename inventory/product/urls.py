import imp
from django.urls import path

from product.views import  ( retrieveProducts, 
        retriveProductsByCategory,
        addProductCategory)

urlpatterns = [
    path('test',retrieveProducts ,name="get_products"),
    path('category',retriveProductsByCategory,name="get_product_by_category"),
    path('category/add/',addProductCategory,name="add_new_category")
]