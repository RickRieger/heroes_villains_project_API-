from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):

  type = request.query_params.get('type')
  


  if request.method == 'GET':
    Supers = Super.objects.all() 
    if type:
      Supers = Supers.filter(super_type__type = type)                    
    serializer = SuperSerializer(Supers, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':   
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk): 
  print(request.data)
  Super = get_object_or_404(Super, pk=pk) 
  if request.method == 'GET': 
    serializer = SuperSerializer(Super)
    return Response(serializer.data) 
  elif request.method == 'PUT':
    serializer = SuperSerializer(Super, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print('==========here=========')
    return Response(serializer.data)
  elif request.method == 'DELETE':
      Super.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)