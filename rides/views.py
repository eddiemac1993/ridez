from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import RideForm

@login_required
def request_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.customer = request.user
            ride.save()
            return redirect('ride_detail', ride_id=ride.id)
    else:
        form = RideForm()
    return render(request, 'rides/request_ride.html', {'form': form})

@login_required
def ride_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'rides/ride_detail.html', {'ride': ride})

@login_required
def driver_rides(request):
    rides = Ride.objects.filter(status='requested')
    return render(request, 'rides/driver_rides.html', {'rides': rides})

@login_required
def accept_ride(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    ride.driver = request.user
    ride.status = 'accepted'
    ride.save()
    return redirect('ride_detail', ride_id=ride.id)
