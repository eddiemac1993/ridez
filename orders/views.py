from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm

@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/place_order.html', {'form': form})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def driver_orders(request):
    orders = Order.objects.filter(status='placed')
    return render(request, 'orders/driver_orders.html', {'orders': orders})

@login_required
def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.driver = request.user
    order.status = 'accepted'
    order.save()
    return redirect('order_detail', order_id=order.id)
