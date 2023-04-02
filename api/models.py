from django.db import models
from rest_framework.decorators import action

# Create your models here.
#Creating Company Model
class Company(models.Model):
    
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=10)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT','IT'),('Non IT', 'Non IT'),('Pharma','Pharma')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    

    def __str__(self):
        return self.name


#Employee Model to be Created.
# This model represents an employee in the system. It contains the following fields:

# employee_id
# : A primary key auto-incrementing integer field.
# name
# : A character field with a maximum length of 50 characters.
# email
# : A character field with a maximum length of 50 characters, unique.
# phone_number
# : A character field with a maximum length of 10 characters, unique.
# address
# : A character field with a maximum length of 200 characters.
# about
# : A text field for a longer description of the employee.
# position
# : A character field with a maximum length of 20 characters. This field has a list of choices from which to select, including 'Manager', 'Software Developer', and 'Program Manager'.
# company
# : A foreign key to the Company model, with a cascade delete.
class Employee(models.Model):
    employee_id: models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    phone_number = models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=200)
    about = models.TextField()
    position = models.CharField(max_length=20, choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Program Manager','pm')
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)


#get current working directory using python
