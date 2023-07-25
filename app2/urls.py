from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
    path('string/',string,name='string'),
]