

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class AddEmployee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, primary_key=True)  
    email = models.EmailField()
    father_name = models.CharField(max_length=100)  
    date_of_birth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    designation = models.CharField(max_length=100)
    higher_education = models.CharField(max_length=100)  
    joining_date = models.DateField()
    
    MARITAL_STATUS_CHOICES = [
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
    ]
    
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES) 
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"  # admin database ki vabeh student information show korbe



class Attendance(models.Model):
    employee_id = models.ForeignKey('AddEmployee', on_delete=models.CASCADE)
    day = models.DateField(null=True)
    
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    
    first_half_attendance = models.CharField(
        max_length=10,
        choices=ATTENDANCE_CHOICES,
        verbose_name="First Half"
    )
    second_half_attendance = models.CharField(
        max_length=10,
        choices=ATTENDANCE_CHOICES,
        verbose_name="Second Half"
    )

    def __str__(self):
        return f"Attendance({self.employee_id}, {self.day})"

   
class EventModel(models.Model):
    event_id =models.CharField(max_length=10, unique=True)
    event_name=models.CharField(max_length=30)
    description=models.TextField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    
    def __str__(self):
        return f"{self.event_name} ({self.event_id})"
    

class LeaveModel(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.ForeignKey(AddEmployee, on_delete=models.CASCADE)  # Removed `null=True`
    
    email = models.EmailField()
    
    LEAVE_STATUS_CHOICES = [
        ('Casual Leave', 'Casual Leave'),
        ('Medical Leave', 'Medical Leave'),
        ('Maternity Leave', 'Maternity Leave'),
        ('Paternity Leave', 'Paternity Leave'),
        ('Bereavement Leave', 'Bereavement Leave'),
        ('Religious Leave', 'Religious Leave'),
        ('Other', 'Other'),
    ]
    
    leave_status = models.CharField(max_length=50, choices=LEAVE_STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"