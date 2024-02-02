from rest_framework import serializers

from .models import *


class DriverSerializer(serializers.ModelSerializer): 
    
    def create(self, validated_data): 
        
        ModelClass = Driver
        try: 
            instance = ModelClass.objects.create(**validated_data) 
        except TypeError: 
            raise TypeError() 
        return instance 
            
    def update(self,instance, validated_data): 
        try: 
            instance.name = validated_data.get('name') 
            instance.last_name = validated_data.get('last_name') 
            instance.email = validated_data.get('email') 
            instance.address= validated_data.get('address') 
            instance.vehicle= validated_data.get('vehicle') 
            instance.save() 
            return instance 
        except TypeError: raise TypeError() 
        
    class Meta: 
        model= Driver 
        fields = '__all__'