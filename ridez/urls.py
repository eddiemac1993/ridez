from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Add this line
    path('users/', include('users.urls')),
    path('rides/', include('rides.urls')),
    path('orders/', include('orders.urls')),
]