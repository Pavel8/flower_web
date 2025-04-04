from django.shortcuts import render, get_object_or_404
from .models import Service
from django.contrib.auth.decorators import login_required, user_passes_test


def service_list(request):
    services = Service.objects.all()
    return render(request, "service_list.html", {"services": services})

def service_detail(request, pk):
    service = get_object_or_404(Service, id=pk)
    return render(request, 'service_detail.html', {'service': service})

def service_create(request):
    return render(request, 'service_form.html')

def service_update(request, pk):
    return render(request, 'service_form.html', {'pk': pk})

def service_delete(request, pk):
    return render(request, 'service_confirm_delete.html', {'pk': pk})

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_service_list(request):
    services = Service.objects.all()
    return render(request, 'staff_service_list.html', {'services': services})