import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Classic.settings import EMAIL_HOST_USER

from .forms import *
from .models import *
from .decorators import *
from django.contrib.auth.models import User


def main_view(req):
    return render(
        req,
        'pages/main.html',
        {
            'services': Services.objects.all()[:10],
            'products': Product.objects.all()[:4]
        }
    )

def about_view(req):
    return render(
        req,
        'pages/about-salon.html',{
            'emp': Employee.objects.all()
        }
    )

def showcase_view(req):
    return render(
        req,
        'pages/showcase.html',
        {
            'products': Product.objects.all()
        }
    )

def contacts_view(req):
    return render(
        req,
        'pages/contacts.html'
    )

def services_view(req):
    return render(
        req,
        'pages/salon_services.html',
        {'services': Services.objects.all()}
    )
@login_required(login_url='login_page')
def record_view(req):
    is_employee = False
    employee = Employee.objects.filter(user=req.user)
    if employee:
        is_employee = True
        record = Record.objects.filter(employee = employee[0])
    else:
        record = Record.objects.filter(user=req.user)
    return render(req, 'pages/record_page.html',{
        'records': record,
        'is_employee': is_employee
    })
@login_required(login_url='login_page')
@client_user
def choose_employee_view(req):
    form = EmployeeForm()
    data = None
    if req.method == 'POST':
        form = EmployeeForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data['employee'].id
            return redirect('choose_service_page', foo=data)
        else:
            form = EmployeeForm()

    return render(req, 'pages/choose_employee_page.html', {
        'form': form,
        'data': data
    })
@login_required(login_url='login_page')
@client_user
def choose_service_view(req, foo):
    form = ServiceForm()
    form.fields['services'].queryset = Employee.objects.get(id=foo).services.all()
    if req.method == 'POST':
        data = int(req.POST['services'][0])
        return redirect('choose_date_page', foo=foo, serv=data)
    return render(req, 'pages/choose_services.html', {
        'form': form
    })
@login_required(login_url='login_page')
@client_user
def choose_date_view(req, foo, serv):
    date = datetime.datetime.now()
    delta = date + datetime.timedelta(30)
    form = DateForm()
    form.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date_input',
                                                                'min': date.strftime('%Y-%m-%d'),
                                                                'max': delta.strftime('%Y-%m-%d')})
    if req.method == 'POST':
        return redirect('choose_time_page', foo=foo, serv=serv, date=req.POST['date'])
    return render(req, 'pages/choose_date_page.html', {
        'form': form
    })
@login_required(login_url='login_page')
def delete_record_view(req, pk):
    record = Record.objects.get(id=pk)
    send_mail('Отмена записи', f'Запись {record.date_record} к {record.employee.user.get_full_name()} на услугу {record.service.name} была отменена.',
              EMAIL_HOST_USER, [record.user.email], fail_silently=False)
    record.delete()
    return redirect('record_page')

def clear_arr_times(records):
    arr_times = [('09:00:00', '09:00'),
                 ('10:00:00', '10:00'),
                 ('11:00:00', '11:00'),
                 ('12:00:00', '12:00'),
                 ('13:00:00', '13:00'),
                 ('14:00:00', '14:00'),
                 ('15:00:00', '15:00'),
                 ('16:00:00', '16:00'),
                 ('17:00:00', '17:00'),
                 ('18:00:00', '18:00')]
    times_str = list(map(lambda x: x.date_record.strftime('%H:%M:%S'), records))
    arr = []
    for elem in arr_times:
        if elem[0] not in times_str:
            arr.append(elem)
    return arr

@login_required(login_url='login_page')
@client_user
def choose_time_view(req, foo, serv, date):
    form = TimeForm()
    employee = Employee.objects.get(id=foo)
    service = Services.objects.get(id=serv)
    user = User.objects.get(id=req.user.id)
    arr_date = date.split('-')
    records = Record.objects.filter(employee=employee, date_record__year =int(arr_date[0]),
                                    date_record__month=int(arr_date[1]), date_record__day=int(arr_date[2]))

    arr_times = clear_arr_times(records)
    form.fields['time'].choices = arr_times
    if req.method == 'POST':
        parse_datetime = datetime.datetime.strptime(f'{date} {req.POST["time"]}', '%Y-%m-%d %H:%M:%S')
        record = Record.objects.create(employee = employee, service = service, user = user, date_record = parse_datetime)
        record.save()

        return redirect('home')

    return render(req, 'pages/choose_time_page.html', {
        'form': form
    })

class RegisterUser(CreateView):
    model = User
    template_name = 'pages/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid

class LoginUser(LoginView):
    model = User
    template_name = 'pages/login.html'
    authentication_form = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class LogOutUser(LogoutView):
    next_page = reverse_lazy('home')