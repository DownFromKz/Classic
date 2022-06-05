from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class AuthUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class EmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label=None, label='')

class ServiceForm(forms.Form):
    services = forms.ModelChoiceField(queryset=None, empty_label=None, label='')

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date_input'}), label='')

class TimeForm(forms.Form):
    time = forms.ChoiceField(label='')