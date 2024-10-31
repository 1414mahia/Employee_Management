from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Updated path to include app name

