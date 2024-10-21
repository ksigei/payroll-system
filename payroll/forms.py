from django import forms
from .models import Salary, Deduction

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['base_salary', 'bonuses', 'allowances', 'deductions']
        widgets = {
            'base_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter base salary'}),
            'bonuses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bonuses'}),
            'allowances': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter allowances'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter deductions'}),
        }

class DeductionForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['deduction_type', 'amount', 'date']
        widgets = {
            'deduction_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter deduction amount'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
