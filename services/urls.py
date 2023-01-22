from django.urls import path
from . import views

urlpatterns = [
    path('activedataentry/', views.ActiveDataEntry, name='activedataentry'),
    path('activedataentry/delete/', views.DeleteEntry, name='delete'),
    path('employeedetails/', views.EmployeeDetails, name='employeedetails'),
]
