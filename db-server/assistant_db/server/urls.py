from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_sensor, name='create_sensor'),
    path('get/', views.get_sensor, name='get_sensor'),
]
