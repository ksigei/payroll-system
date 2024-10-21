from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Sum
from .models import Employee, Salary, Deduction
from .forms import SalaryForm, DeductionForm  # We will create these forms

def dashboard(request):
    # Fetch salary data
    total_salaries = Salary.objects.aggregate(total_salary=Sum('base_salary'))
    total_deductions = Deduction.objects.aggregate(total_deductions=Sum('amount'))
    
    # Calculate total employees
    total_employees = Employee.objects.count()  # Adjust the model name if it's different

    context = {
        'total_salaries': total_salaries['total_salary'] or 0,
        'total_deductions': total_deductions['total_deductions'] or 0,
        'net_salary': (total_salaries['total_salary'] or 0) - (total_deductions['total_deductions'] or 0),
        'total_employees': total_employees,
    }

    return render(request, 'payroll/dashboard.html', context)

# List all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'payroll/employee_list.html', {'employees': employees})

# View salary details for a specific employee
def employee_salary(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    salaries = Salary.objects.filter(employee=employee)
    return render(request, 'payroll/employee_salary.html', {'employee': employee, 'salaries': salaries})

# Add salary record for an employee
def add_salary(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.employee = employee
            salary.save()
            return redirect('employee_salary', employee_id=employee.id)
    else:
        form = SalaryForm()

    return render(request, 'payroll/add_salary.html', {'form': form, 'employee': employee})

# Add deduction record for an employee
def add_deduction(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = DeductionForm(request.POST)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.employee = employee
            deduction.save()
            return redirect('employee_salary', employee_id=employee.id)
    else:
        form = DeductionForm()

    return render(request, 'payroll/add_deduction.html', {'form': form, 'employee': employee})

# View overall payroll summary
def payroll_summary(request):
    salaries = Salary.objects.all()
    total_salaries = sum(salary.net_salary for salary in salaries)
    return render(request, 'payroll/payroll_summary.html', {'salaries': salaries, 'total_salaries': total_salaries})
