import uuid
from django.db import models
from django.core.validators import EmailValidator

class Employee(models.Model):
    class Department(models.TextChoices):
        HR = 'HR'
        ENGINEERING = 'Engineering'
        SALES = 'Sales'
        FINANCE = 'Finance'
        OPERATION = 'Opeartion'
    
    name =  models.CharField(
        max_length=200, 
        blank=False, 
        null=False, 
        help_text="Employee's full name")
    
    email = models.CharField(
        unique=True, 
        null=False, 
        validators=[EmailValidator()], 
        help_text="Email Address")
    
    department = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        choices=Department.choices, 
        help_text="Job Department (e.g., 'HR', 'Engineering', 'Sales')")
    
    role = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Job Role(e.g., 'Manager', 'Developer','Analyst')")
    
    date_joined = models.DateField(
        auto_now_add=True,
        help_text="Date when an employee was added")

    def __str__(self):
        return f"{self.name} ({self.email})"
