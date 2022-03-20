from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from powers.models import Power
from powers.serializers import PowersSerializer


@api_view(['GET', 'POST'])
def supers_list(request):

  type = request.query_params.get('type')
  
  if request.method == 'GET':
    supers = Super.objects.all() 
    if type:
      supers = supers.filter(super_type_id__type = type)                    
      serializer = SuperSerializer(supers, many=True)
      return Response(serializer.data)
    else: 
      heros = supers.filter(super_type_id__type = 'hero')
      villains = supers.filter(super_type_id__type = 'villain')
    
      heros = SuperSerializer(heros, many=True)
      villains = SuperSerializer(villains, many=True)
      result = {'heros':heros.data, 'villains':villains.data}
      return Response(result)


  elif request.method == 'POST':   
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk): 
  super = get_object_or_404(Super, pk=pk)
  power = request.query_params.get('power')
 
  if request.method == 'GET': 
    serializer = SuperSerializer(super)
    return Response(serializer.data) 
  elif request.method == 'PUT':
    if power:
      new_power = Power(name=power)
      new_power.save()
      super.power.add(new_power)
      serializer = SuperSerializer(super)
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:  
      serializer = SuperSerializer(super, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
      super.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)