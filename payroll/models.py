from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.net_salary = self.base_salary + self.bonuses + self.allowances - self.deductions
        super(Salary, self).save(*args, **kwargs)

    def __str__(self):
        return f"Salary for {self.employee.first_name} {self.employee.last_name}"

class Deduction(models.Model):
    type_choices = [
        ('LOAN', 'Loan'),
        ('TAX', 'Tax'),
        ('INSURANCE', 'Insurance'),
        ('Helb', 'Helb'),
        ('NSSF', 'NSSF'),
        ('NHIF', 'NHIF'),
        ('OTHER', 'Other'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deduction_type = models.CharField(max_length=100, choices=type_choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Deduction: {self.deduction_type} for {self.employee.first_name} {self.employee.last_name}"
