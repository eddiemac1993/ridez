from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_ride, name='request_ride'),
    path('<int:ride_id>/', views.ride_detail, name='ride_detail'),
    path('driver/', views.driver_rides, name='driver_rides'),
    path('accept/<int:ride_id>/', views.accept_ride, name='accept_ride'),
]