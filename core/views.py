from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def business_terms_conditions(request):
    return render(request, 'services/business_terms_conditions.html')
