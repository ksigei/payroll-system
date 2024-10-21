from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/salary/', views.employee_salary, name='employee_salary'),
    path('employees/<int:employee_id>/add-salary/', views.add_salary, name='add_salary'),
    path('employees/<int:employee_id>/add-deduction/', views.add_deduction, name='add_deduction'),
    path('payroll-summary/', views.payroll_summary, name='payroll_summary'),
]
