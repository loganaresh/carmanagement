from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Car, Service, Insurance

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
