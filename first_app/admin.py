

# Register your models here.
from django.contrib import admin
from .models import AddEmployee, LeaveModel, Attendance, EventModel
# Register your models here.
admin.site.register(AddEmployee)

admin.site.register(Attendance)

admin.site.register(EventModel)

admin.site.register( LeaveModel)