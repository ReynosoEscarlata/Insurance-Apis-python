# DJANGO
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
# REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# HELPERS
from kiva_test_rrr.helpers.commonFunctions import log


# Create your views here.
class RegisterUser(APIView):

    def get(self,request):
        context={}
        log("Test","GET",2,"Start get method")
        return Response(context, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            log("RegisterUser","POST",2,"Create user class")
            context={}
            data = request.data
            user = User.objects.create_user(data.get("email"), data.get("email"), data.get("password"))
            user.save()
            if user:
                context={"message":"User has been created"}
                log("RegisterUser","POST",2,f"User created, user: {user}")
                log("RegisterUser","POST",2,"Add user to group")
                group = Group.objects.get(name=data.get("role"))
                if group:
                    log("RegisterUser","POST",2,"Group added to user")
                    user.groups.add(group)
                else:
                    log("RegisterUser","POST",3,"Group not found")


            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as error:
            context={"message":"Occurs an error trying to create the user"}
            log("RegisterUser","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginUser(APIView):

    def get(self,request):
        context={}
        return Response(context, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            log("LoginUser","POST",2,"Log in user")
            context={}
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context = {"message":"You are logged in"}
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {"message":"Bad credentials"}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            log("LoginUser","POST",4,f"Occurs an error: {error}")

            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutUser(APIView):

    def get(self,request):
        context={}
        return Response(context, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            context={}
            context = {"message":"You are logged out"}
            logout(request)
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            log("RegisterUser","POST",4,f"Occurs an error: {error}")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)