from django.shortcuts import render

# REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# HELPERS
from kiva_test_rrr.helpers.commonFunctions import log
from kiva_test_rrr.decorators.user import ManagerRequired


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
    
class Driver(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)
    
class Vehicle(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)
    
class InsuranceAply(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method token")
        return Response(context, status=status.HTTP_200_OK)