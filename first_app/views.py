
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import  auth
from .forms import AddLeaveForm, EventForm, LoginForm, AddEmployeeForm ,AttendanceForm
from .models import AddEmployee, LeaveModel, Attendance, EventModel
from .import forms
from first_app import models
from django.contrib import messages

from django.contrib.auth import logout


def home(request):
    return render(request, 'index.html')

# Handle login
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password) # databese a user ache naki check korbo

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('main_dashboard')  # Redirect to Add Employee page
              
            
            
    return render(request, 'login.html', {'form': form})




def register(request):
   if request.method =='POST':
        
      registration_form =forms.RegistrationForm(request.POST) # form class er AuthorFrom
      if registration_form.is_valid():
         registration_form.save()
         messages.success(request,"Account created successfully")
         return redirect("login_page")
      
   else:
      registration_form =forms.RegistrationForm() # user website a dhukche but kono data pass kore nai
   return render(request,'register.html',{'form':registration_form,})


def  dashboard(request):
    return render(request, 'main_dashboard.html')

def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            
            return redirect('view_employee')  # Redirect to view employee page
    else:
        form = AddEmployeeForm()  # Empty form for GET request

    return render(request, 'add_employee.html', {'form': form})

def view_employee(request):
 
    emp = AddEmployee.objects.all()
        
    return render(request, 'view_employee.html', {'data': emp})


def delete_employee(request, id):
    # Get the employee by employee_id or return 404 if not found
    emp = get_object_or_404(AddEmployee, employee_id=id)
    emp.delete()  # Delete the employee
   
    return redirect('view_employee')

def update_employee(request, employee_id):
    # Get the employee by employee_id or return 404 if not found
    employees = get_object_or_404(AddEmployee, employee_id=employee_id)

    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()  # Save changes to the database
          
            return redirect('view_employee')
    else:
        form = AddEmployeeForm(instance=employees)  # Pre-fill form with employee data for GET requests

    return render(request, 'update_employee.html', {'employees': employees, 'form': form})

def add_attendance(request):
    if request.method =='POST':
        attendance_form =forms.AttendanceForm(request.POST,)
        if attendance_form.is_valid():
           attendance_form.save()
           return redirect("view_attendance")
    else:
           
     attendance_form =forms.AttendanceForm()
    return render(request,'add_attendance.html',{'form': attendance_form})


def view_attendance(request):
    emp = Attendance.objects.all()  # Get all employees from the database
    return render(request, 'view_attendance.html', {'data': emp})




   
def add_event(request):
    if request.method =="POST":
        form =forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_event")
    else:
           form =forms.EventForm()
    return render(request,"add_event.html",{'form':form})

def view_event(request):
    event = EventModel.objects.all()
    return render(request,"view_event.html",{'data':event})

def delete_event(request, event_id):
    
    ev= models.EventModel.objects.get(event_id=event_id)
    ev.delete()  # Delete the employee
   
    return redirect('view_event')



def update_event(request, event_id):
    event = get_object_or_404(EventModel, event_id=event_id)
    

    if request.method == 'POST':
        event_form = forms.EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            return redirect('view_event')
    else:
        event_form = forms.EventForm(instance=event)

    return render(request, 'update_event.html', {'event':event,'form': event_form})

def add_leave(request):
    if request.method =="POST":
        form =forms.AddLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            print("Leave data saved successfully.")
            return redirect("view_leave")
    else:
        form =forms.AddLeaveForm()
    return render(request,'add_leave.html',{'form':form})


def view_leave(request):
    leave=LeaveModel.objects.all()
   
    return render(request,'view_leave.html',{'data':leave})



def Logout(request):
    logout(request)
    return redirect("home")