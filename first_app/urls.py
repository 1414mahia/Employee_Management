from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main_dashboard/', views.dashboard, name='main_dashboard'),
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
    
    path('add_employee/', views.add_employee, name='add_employee'),
    path('view_employee/', views.view_employee, name='view_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),  # Add trailing slash
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    
    path('add_event/',views.add_event,name="add_event"),
    path('view_event/',views.view_event,name="view_event"),
   # path('update_event/<int:event_id>/', views.update_event, name='update_event_page'),
   # path('delete_event/<int:event_id>/', views.delete_event, name='delete_event_page'),
    path('add_leave/',views.add_leave, name="add_leave"),
    path('view_leave/',views.view_leave, name="view_leave"),
   
    path('logout/', views.Logout, name='logout'),
   
]
