from django.urls import re_path

from .views import *


urlpatterns = [
    re_path(r'test[|/]', TestRole.as_view(), name="test"),
    re_path(r'test-token[|/]', TestToken.as_view(), name="test-token"),
    re_path(r'driver[|/]', DriverView.as_view(), name="driver-view"),
    re_path(r'create-vehicle[|/]', CreateVehicle.as_view(), name="create-vehicle"),
    re_path(r'create-insurance[|/]', CreateInsuranceAply.as_view(), name="create-insurance"),
]