from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.Employee_form, name='Emp_form'),
    path('form/<int:id>', views.Employee_form, name='Emp_update'),
    path('list/', views.Employee_list, name='Emp_list'),
    path('delete/<int:id>', views.Employee_delete, name='Emp_delete'),
]