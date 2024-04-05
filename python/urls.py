from django.urls import path,include
from python.views import *
app_name="python"

urlpatterns = [
    path('pythondeveloper/',pythondeveloper,name="pythondeveloper"),
]
