from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('driver/', views.driver_orders, name='driver_orders'),
    path('accept/<int:order_id>/', views.accept_order, name='accept_order'),
]
