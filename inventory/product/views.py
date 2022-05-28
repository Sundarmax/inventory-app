import imp
from itertools import product
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.serializer import ProductSerializer,ProductCategorySerializer
from product.models import Product

@api_view(('GET','POST',))
def retrieveProducts(request):
    if request.method == "GET":
        # Get queryset objects for project model 
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

@api_view(('GET','POST',))
def retriveProductsByCategory(request):
    if request.method == "GET":
        # Get queryset objects for project model with filter.
        queryset = Product.objects.filter(product_supplier=2)
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

@api_view(['POST',])
def addProductCategory(request):
    if request.method == 'POST':
        # add new prodcut category
        res = {}
        status_code = 200
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res.update({"data":serializer.data})
        else:
            status_code = 400
            res["error"] = serializer.errors
        return Response(res)