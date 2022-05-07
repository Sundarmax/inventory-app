import imp
from django.urls import path

from product.views import retrieveProducts

urlpatterns = [
    path('test',retrieveProducts ,name="get_products"),
]
