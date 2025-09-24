from home.views import *
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('emp/', employee, name='employee'),
]