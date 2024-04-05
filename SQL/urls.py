from django.urls import path
from SQL.views import *
app_name='SQL'
urlpatterns = [
    path('sqldeveloper',sqldeveloper,name='sqldeveloper'),
]
