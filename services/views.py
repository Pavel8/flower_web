from django.shortcuts import render

def service_list(request):
    return render(request, 'service_list.html')

def service_detail(request, pk):
    return render(request, 'service_detail.html', {'pk': pk})

def service_create(request):
    return render(request, 'service_form.html')

def service_update(request, pk):
    return render(request, 'service_form.html', {'pk': pk})

def service_delete(request, pk):
    return render(request, 'service_confirm_delete.html', {'pk': pk})
