from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Car, Service, Insurance
from django.contrib.auth import get_user_model
User = get_user_model()
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    role = request.user.role
    if role == 'Manager':
        return redirect('manager_dashboard')
    elif role == 'Employee':
        return redirect('employee_dashboard')
    elif role == 'Mechanic':
        return redirect('mechanic_dashboard')
    elif role == 'Customer':
        return redirect('customer_dashboard')

@login_required
@user_passes_test(lambda u: u.role == 'Manager')
def manager_dashboard(request):
    cars = Car.objects.all()
    employees = User.objects.filter(role='Employee')
    customers = User.objects.filter(role='Customer')
    orders = []  # Add logic to track orders
    return render(request, 'manager_dashboard.html', {
        'cars': cars,
        'employees': employees,
        'customers': customers,
        'orders': orders
    })

@login_required
@user_passes_test(lambda u: u.role == 'Employee')
def employee_dashboard(request):
    cars = Car.objects.all()
    services = Service.objects.all()
    return render(request, 'employee_dashboard.html', {
        'cars': cars,
        'services': services
    })

@login_required
@user_passes_test(lambda u: u.role == 'Mechanic')
def mechanic_dashboard(request):
    services = Service.objects.all()
    return render(request, 'mechanic_dashboard.html', {
        'services': services
    })

@login_required
@user_passes_test(lambda u: u.role == 'Customer')
def customer_dashboard(request):
    user_services = Service.objects.filter(car__customer=request.user)
    insurances = Insurance.objects.filter(car__customer=request.user)
    return render(request, 'customer_dashboard.html', {
        'user_services': user_services,
        'insurances': insurances
    })
