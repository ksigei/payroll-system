import random
from django.core.management.base import BaseCommand
from payroll.models import Employee, Salary

class Command(BaseCommand):
    help = 'Seed the database with employees and salaries'

    def handle(self, *args, **kwargs):
        self.seed_employees()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))

    def seed_employees(self):
        # Grouped by tribe: Kikuyu, Luo, and Kalenjin
        tribes = {
            'Kikuyu': {
                'first_names': ['James', 'Wanjiku', 'Peter', 'Mwangi', 'Mary', 'Nyokabi', 'Samuel', 'Muthoni'],
                'last_names': ['Kimani', 'Wairimu', 'Mwangi', 'Muriuki', 'Njoroge', 'Maina', 'Mwaniki']
            },
            'Luo': {
                'first_names': ['John', 'Amina', 'Otieno', 'Alice', 'Joseph', 'Grace', 'Okoth', 'Odhiambo'],
                'last_names': ['Ochieng', 'Odhiambo', 'Onyango', 'Otieno', 'Omondi', 'Owino']
            },
            'Kalenjin': {
                'first_names': ['Kiprono', 'Cherono', 'Kipchumba', 'Kibet', 'Kiptoo', 'Chepkorir', 'Kipkirui'],
                'last_names': ['Koech', 'Kiprotich', 'Chepkorir', 'Kiptoo', 'Kipng\'etich', 'Kipkemoi']
            }
        }

        positions = [
            'Software Engineer', 'HR Manager', 'Accountant', 'Marketing Manager', 'Operations Officer',
            'Data Analyst', 'Sales Executive', 'Finance Manager', 'Customer Support', 'IT Support'
        ]
        departments = ['IT', 'Human Resources', 'Finance', 'Sales', 'Operations', 'Customer Support']

        tribe_choices = list(tribes.keys())

        # Seed 20 employees, keeping consistency in names from the same tribe
        for i in range(20):
            selected_tribe = random.choice(tribe_choices)
            first_name = random.choice(tribes[selected_tribe]['first_names'])
            last_name = random.choice(tribes[selected_tribe]['last_names'])
            position = random.choice(positions)
            department = random.choice(departments)

            # Generate a unique email address for each employee
            email = f"{first_name.lower()}.{last_name.lower()}{i}@example.com"

            # Create Employee
            employee = Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                position=position,
                department=department,
                email=email  # Ensure this is unique
            )

            # Generate salary data
            base_salary = random.randint(50000, 150000)
            bonuses = random.randint(5000, 20000)
            allowances = random.randint(5000, 15000)
            deductions = random.randint(1000, 10000)

            Salary.objects.create(
                employee=employee,
                base_salary=base_salary,
                bonuses=bonuses,
                allowances=allowances,
                deductions=deductions,
                net_salary=(base_salary + bonuses + allowances - deductions),
                payment_date='2024-09-01'
            )
