from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('about', about),
    path('team', team),

]