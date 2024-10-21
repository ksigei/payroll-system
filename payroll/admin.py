from django.contrib import admin
from .models import Employee, Salary, Deduction

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Deduction)
