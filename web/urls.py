from django.urls import path
from web.views import *
app_name='web'

urlpatterns = [
    path('webdeveloper/',webdeveloper,name='webdeveloper'),
]
