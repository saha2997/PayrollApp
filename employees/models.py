

# Learn:

# Models
# Migrations
# Admin Panel
# ORM
from enum import unique
from django.db import models
# Employee Model
# Fields:
# employee_id
# first_name
# last_name
# email
# phone
# date_of_joining
# department
# designation
# status

class Employee(models.Model):
    STATUS_CHOICE = [("ACTIVE","Active"),
                    ("INACTIVE", "Inactive"),
                    ("TERMINATED", "Terminated"),
    ]
    employee_id = models.CharField(max_length=20,unique = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length= 200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 15)
    date_of_joining = models.DateField(auto_now_add= True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices= STATUS_CHOICE,default = "Active")



# Create your models here.
  