from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import StaffLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test


def staff_login(request):
    form = StaffLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('staff_dashboard')  # nebo jiná stránka
        else:
            form.add_error(None, "Neplatné přihlašovací údaje nebo nemáte oprávnění.")

    return render(request, 'login.html', {"form": form})

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')