from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.main_view, name = 'home'),
    path('about', about_view, name = 'about'),
    path('services', services_view, name = 'services'),
    path('showcase',views.showcase_view, name = 'showcase'),
    path('contacts',views.contacts_view, name = 'contacts'),
    path('register', RegisterUser.as_view(), name = 'register_page'),
    path('login', LoginUser.as_view(), name = 'login_page'),
    path('logout', LogOutUser.as_view(), name = 'logout_page'),
    path('record', record_view, name = 'record_page'),
    path('choose_employee', choose_employee_view, name = 'choose_employee_page'),
    path('choose_service/<foo>', choose_service_view, name = 'choose_service_page'),
    path('choose_date/<foo>/<serv>', choose_date_view, name='choose_date_page'),
    path('choose_time/<foo>/<serv>/<date>', choose_time_view, name='choose_time_page'),
    path('delete_record/<int:pk>', delete_record_view, name='delete_record'),
]