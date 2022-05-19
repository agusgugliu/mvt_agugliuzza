from django.urls import path
from APP_Familia.views import index

urlpatterns = [
    path('index/', index),
]