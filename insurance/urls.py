from django.urls import re_path

from .views import *


urlpatterns = [
    re_path(r'test[|/]', TestRole.as_view(), name="test"),
    re_path(r'test-token[|/]', TestToken.as_view(), name="test-token"),
    re_path(r'driver[|/]', DriverView.as_view(), name="driver-view"),
    re_path(r'vehicle[|/]', VehicleView.as_view(), name="vehicle-view"),
    re_path(r'application[|/]', InsuranceApplyView.as_view(), name="application-view"),
]