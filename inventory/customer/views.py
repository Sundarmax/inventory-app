import imp
from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.decorators import api_view
from customer.serializer import *
from rest_framework.response import Response


@api_view(['POST'])
def addCustomer(request):
    res = {}
    status_code = 200 
    serializer = customerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res["data"] = serializer.data
    else:
        res["error"] =serializer.errors
    return Response(res,status_code)

