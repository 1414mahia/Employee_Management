from django import forms
from .models import AddEmployee
from  .models import Attendance
from .models import EventModel
from .models import LeaveModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = AddEmployee
        fields = ['name', 'employee_id', 'email', 'father_name', 
                  'date_of_birth', 'salary', 'designation', 
                  'higher_education', 'joining_date', 
                  'marital_status', 'nationality']  # Specify the fields explicitly
        labels = {
            'name': 'Name',
            'employee_id': 'Employee ID',
            'email': 'Email',
            'father_name': 'Father\'s Name',
            'date_of_birth': 'Date of Birth',
            'salary': 'Salary',
            'designation': 'Designation',
            'higher_education': 'Higher Education',
            'joining_date': 'Joining Date',
            'marital_status': 'Marital Status',
            'nationality': 'Nationality',
        }
        help_texts = {
            'name':'Enter Your Name',
            'salary': 'Use the format: 99999.99',
        }




class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    
 
 
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance  
        fields = '__all__' 
        
        
class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel  # Reference the actual model class, not a string
        fields = ['event_id', 'event_name', 'description', 'start_date', 'end_date'] 





class AddLeaveForm(forms.ModelForm):
    class Meta:
        model = LeaveModel
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

#The widgets dictionary is used to specify which HTML input elements should be used for
# each field in the form
       
    

