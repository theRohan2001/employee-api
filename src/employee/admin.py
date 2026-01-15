from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin interface for Employee model.
    """
    list_display = ['id', 'name', 'email', 'department', 'role', 'date_joined']
    list_filter = ['department', 'role', 'date_joined']
    search_fields = ['name', 'email', 'department', 'role']
    readonly_fields = ['date_joined']
    ordering = ['-date_joined']

