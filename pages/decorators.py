from django.shortcuts import redirect
from .models import Employee

def client_user(view_func):
    def wrapper_func(req, *args, **kwargs):
        employees = list(map(lambda x: x.user, Employee.objects.all()))
        if req.user not in employees:
            return view_func(req, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func

def employee_user(view_func):
    def wrapper_func(req, *args, **kwargs):
        employees = list(map(lambda x: x.user, Employee.objects.all()))
        if req.user in employees:
            return view_func(req, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func