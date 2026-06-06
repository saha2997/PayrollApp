from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Employee

class Employeeadmin(admin.ModelAdmin):
    list_display = (
        
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "department",
        "designation",
        "status",
    )
    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "department",
        "designation",
        "status",
    )

    ordering = (
        "employee_id",
    )
# Register your models here.
admin.site.register(Employee, Employeeadmin)
