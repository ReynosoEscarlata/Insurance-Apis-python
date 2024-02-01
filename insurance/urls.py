from django.urls import re_path

from .views import *


urlpatterns = [
    re_path(r'test[|/]', TestRole.as_view(), name="test"),
    re_path(r'test-token[|/]', TestToken.as_view(), name="test")
]