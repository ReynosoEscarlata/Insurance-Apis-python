from django.shortcuts import render

# REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# HELPERS
from kiva_test_rrr.helpers.commonFunctions import log
from kiva_test_rrr.decorators.user import ManagerRequired
# SERIALIZERS
from .serializers import *


# Create your views here.
class TestRole(ManagerRequired, APIView):

    def get( self,request):
        context={}
        log("Test","GET",2,"Start get method")
        return Response(context, status=status.HTTP_200_OK)

class TestToken(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)
    
class DriverView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            context={}
            log("CreateDriver","GET",2,"Start GET method to get drivers")
            get_all_drivers = Driver.objects.all().values()
            context = {
                "drivers":get_all_drivers
            }
            return Response(context, status=status.HTTP_200_OK)
            
        except Exception as error:
            log("DriverView","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
            context={}
            log("DriverView","POST",2,"Start POST method to create a driver")
            create_driver = DriverSerializer(data = request.POST)
            if create_driver.is_valid():
                create_driver.save()
                log("DriverView","POST",2,"A driver has been created")
            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as error:
            log("DriverView","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request):
        try:
            context={}
            log("DriverView","PUT",2,"Start PUT method to edit a driver")
            get_driver = Driver.objects.filter(id=request.POST["id"]).first()
            create_driver = DriverSerializer(get_driver, data = request.POST)
            if create_driver.is_valid():
                create_driver.save()
                log("DriverView","PUT",2,"A driver has been edited")
            return Response(context, status=status.HTTP_202_ACCEPTED)
        except Exception as error:
            log("DriverView","PUT",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
class CreateVehicle(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)
    
class CreateInsuranceAply(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)