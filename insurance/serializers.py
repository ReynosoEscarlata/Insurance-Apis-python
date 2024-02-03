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



class VehicleSerializer(serializers.ModelSerializer): 
    
    def create(self, validated_data): 
        ModelClass = Vehicle
        try: 
            instance = ModelClass.objects.create(**validated_data) 
        except TypeError: 
            raise TypeError() 
        return instance 
            
    def update(self,instance, validated_data): 
        try: 
            instance.brand = validated_data.get('brand') 
            instance.model = validated_data.get('model') 
            instance.year = validated_data.get('year') 
            instance.serial_number= validated_data.get('serial_number')
            instance.save() 
            return instance 
        except TypeError: raise TypeError() 
        
    class Meta: 
        model= Vehicle 
        fields = '__all__'
        
class InsuranceApplicationSerializer(serializers.ModelSerializer): 
            
    def update(self, instance, validated_data): 
        
        try: 
            instance.active_status = validated_data.get('active_status')
            instance.user = validated_data.get('user')
            instance.save() 
            return instance 
        except TypeError: raise TypeError() 
        
    class Meta: 
        model= InsuranceApplication 
        fields = '__all__'
        
class InsuranceApplicationCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data): 
            ModelClass = InsuranceApplication
            try: 
                instance = ModelClass.objects.create(**validated_data) 
            except TypeError: 
                raise TypeError() 
            return instance 
    class Meta: 
        model= InsuranceApplication 
        exclude= ('active_status',)

class InsuranceStatusSerializer(serializers.ModelSerializer): 
    
    def create(self, validated_data): 
        ModelClass = InsuranceStatus
        try: 
            instance = ModelClass.objects.create(**validated_data) 
        except TypeError: 
            raise TypeError() 
        return instance 
            
    def update(self,instance, validated_data): 
        try: 
            instance.status = validated_data.get('status')
            instance.save() 
            return instance 
        except TypeError: raise TypeError() 
        
    class Meta: 
        model= InsuranceStatus 
        fields = '__all__'