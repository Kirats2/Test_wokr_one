from django import forms
from .models import Employee, Department, Position


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class AddPositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
