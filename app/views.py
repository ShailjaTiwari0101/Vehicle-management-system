from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Vehicle
from .forms import VehicleForm

def is_superadmin(user):
    return user.is_superuser or user.groups.filter(name='Super Admin').exists()

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_user(user):
    return user.groups.filter(name='User').exists()

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles,
        'is_superadmin': is_superadmin(request.user),
        'is_admin': is_admin(request.user),
        'is_user': is_user(request.user),
    }
    return render(request, 'vehicle_list.html', context)

@user_passes_test(is_superadmin)
def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicle_form.html', {'form': form})

@user_passes_test(lambda u: is_superadmin(u) or is_admin(u))
def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicle_form.html', {'form': form})

@user_passes_test(is_superadmin)
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicle_confirm_delete.html', {'vehicle': vehicle})
