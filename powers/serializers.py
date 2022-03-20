from rest_framework import serializers
from .models import Power

class PowersSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Power
    fields = ['id','name']
  