from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PowersSerializer
from supers.serializers import SuperSerializer
from .models import Power
from supers.models import Super


@api_view(['POST', 'GET'])
def powers_list(request):

  power = request.query_params.get('power')
  
  if request.method == 'GET':
    powers = Power.objects.all()                    
    serializer = PowersSerializer(powers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':   
    serializer = PowersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def powers_detail(request, pk): 
  super = get_object_or_404(Power, pk=pk) 
  if request.method == 'GET': 
    serializer = PowersSerializer(super)
    return Response(serializer.data) 
  elif request.method == 'PUT':
    serializer = PowersSerializer(super, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
      super.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)