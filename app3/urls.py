from django.urls import path
from app3.views import *

app_name='anything'

urlpatterns=[
    path('fifth/',fifth,name='fifth'),
    path('sixth/',sixth,name='sixth'),
    path('string/',string,name='string'),
]