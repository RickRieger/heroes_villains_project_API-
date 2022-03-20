from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Super
    fields = ['id','name', 'alter_ego', 'power', 'catchphrase', 'super_type']
    depth = 1