from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
# REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# HELPERS
from kiva_test_rrr.helpers.commonFunctions import log, is_authorized
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
            log("DriverView","GET",2,"Start GET method to get drivers")
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
    
class VehicleView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            context={}
            log("VehicleView","GET",2,"Start GET method to get vehicles")
            get_all_vehicles = Vehicle.objects.all().values()
            context = {
                "vehicles":get_all_vehicles
            }
            return Response(context, status=status.HTTP_200_OK)
            
        except Exception as error:
            log("VehicleView","GET",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request):
        try:
            context={}
            log("VehicleView","POST",2,"Start POST method to create a vehicle")
            create_vehicle = VehicleSerializer(data = request.POST)
            print(create_vehicle)
            if create_vehicle.is_valid():
                create_vehicle.save()
                log("VehicleView","POST",2,"A vehicle has been created")
            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as error:
            log("VehicleView","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request):
        try:
            context={}
            log("VehicleView","PUT",2,"Start PUT method to edit a vehicle")
            get_vehicle = Vehicle.objects.filter(id=request.POST["id"]).first()
            edit_vehicle = VehicleSerializer(get_vehicle, data = request.POST)
            if edit_vehicle.is_valid():
                edit_vehicle.save()
                log("VehicleView","PUT",2,"A vehicle has been edited")
            return Response(context, status=status.HTTP_202_ACCEPTED)
        except Exception as error:
            log("VehicleView","PUT",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InsuranceApplyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            context={}
            log("InsuranceApplyView","GET",2,"Start GET method to get applications")
            Insurance_application = InsuranceApplication.objects.all().values()
            context = {
                "Insurance_application":Insurance_application
            }
            return Response(context, status=status.HTTP_200_OK)
            
        except Exception as error:
            log("InsuranceApplyView","GET",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        try:
            context={}
            log("InsuranceApplyView","POST",2,"Start POST method to create an application")
            data = request.POST.copy()
            data['user']=request.user.id
            create_insurance_application = InsuranceApplicationCreateSerializer(data = data)
            
            if create_insurance_application.is_valid():
                create_insurance_application.save()
                log("InsuranceApplyView","POST",2,"An application has been created")
                # CRETAE HISTORY STATUS
                history_object={
                    "status":"SUBMISSION",
                    "insurance_application":create_insurance_application.data['id']
                }
                create_history_status = InsuranceStatusSerializer(data=history_object)
                if create_history_status.is_valid():
                    create_history_status.save()
                    log("InsuranceApplyView","POST",2,"An history status has been created")
                    
            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as error:
            log("InsuranceApplyView","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request):
        try:
            context={}
            log("InsuranceApplyView","POST",2,"Start PUT method to edit an application")
            data = request.POST.copy()
            data['user']=request.user.id
            get_application = InsuranceApplication.objects.filter(id=data['id']).first()
            
            if is_authorized(request, data) is False:
                return Response(context, status=status.HTTP_401_UNAUTHORIZED)
            
            create_insurance_application = InsuranceApplicationSerializer(get_application, data = data)
            if create_insurance_application.is_valid():
                create_insurance_application.save()
                log("InsuranceApplyView","PUT",2,"An application has been updated")
                # CRETAE HISTORY STATUS
                history_object={
                    "status":data['active_status'],
                    "insurance_application":data['id'],
                }
                create_history_status = InsuranceStatusSerializer(data=history_object)
                if create_history_status.is_valid():
                    create_history_status.save()
                    log("InsuranceApplyView","POST",2,"An history status has been created")
                    return Response(context, status=status.HTTP_201_CREATED)
                else:
                    log("InsuranceApplyView","POST",2,"Form is not correct")
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                log("InsuranceApplyView","POST",2,"Form is not correct")
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
                 
        except Exception as error:
            log("InsuranceApplyView","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)