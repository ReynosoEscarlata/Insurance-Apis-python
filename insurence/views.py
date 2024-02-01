from django.shortcuts import render

# REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# HELPERS
from kiva_test_rrr.helpers.commonFunctions import log

# Create your views here.
class Test(APIView):

    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method")
        return Response(context, status=status.HTTP_200_OK)