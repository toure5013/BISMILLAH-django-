
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('basket', views.basketball),
    path('hand', views.handball),
    path('foot', views.football)
]