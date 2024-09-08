from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('mechanic_dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
]
