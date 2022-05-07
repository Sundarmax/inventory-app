import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.serializer import ProductSerializer
from product.models import Product

@api_view(('GET','POST',))
def retrieveProducts(request):
    if request.method == "GET":
        # Get project model queryset objects. 
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data,status=200)
