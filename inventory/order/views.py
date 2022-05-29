from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import *
from order.models import *
from order.serializers import *

class addNewOrder(APIView):

    def get(self,request):
        # which returns all record info in db
        obj = Order.objects.all()
        Serializer = OrderSerializer(obj,many=True)
        return Response(Serializer.data)
    
    def post(self,request):
        _payload = request.data.copy()
        Serializer = OrderSerializer(data=_payload)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        else:
            return Response(Serializer.errors,status=400)
