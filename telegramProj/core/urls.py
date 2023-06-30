from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('check_unique_email/', check_unique_email, name='check_unique_email'),
    path('check_unique_phone/', check_unique_phone, name='check_unique_phone'),
]