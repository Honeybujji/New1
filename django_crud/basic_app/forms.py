from .models import Position, Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta():
        model  = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = '--Select--'