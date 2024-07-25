from django.db import models
from users.models import CustomUser

class Order(models.Model):
    STATUS_CHOICES = (
        ('placed', 'Placed'),
        ('accepted', 'Accepted'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_orders')
    driver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='driver_orders')
    restaurant = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='placed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)