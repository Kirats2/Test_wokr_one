from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department, Position, Employee
from .forms import AddPositionForm, AddDepartmentForm, AddEmployeeForm
from django.urls import reverse_lazy


def index(request):
    return render(request, "index.html")


class DepartmentListView(ListView):
    model = Department
    queryset = Department.objects.all()
    paginate_by = 10


class DepartmentCreateView(CreateView):
    form_class = AddDepartmentForm
    template_name = 'department_create.html'
    success_url = '/department/'


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_delete.html'
    success_url = reverse_lazy('department_list_url')


class PositionListView(ListView):
    model = Position
    queryset = Position.objects.all()
    paginate_by = 10


class PositionCreateView(CreateView):
    form_class = AddPositionForm
    template_name = 'position_create.html'
    success_url = '/position/'

class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'position_delete.html'
    success_url = reverse_lazy('position_list_url')



class EmployeeListView(ListView):
    model = Employee
    queryset = Employee.objects.all()
    paginate_by = 10

    def get_queryset(self):
        return Employee.objects.all().select_related('employment_position').select_related('employment_department')


class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'card'





class EmployeeCreateView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employee_create.html'
    success_url = '/employee/'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_update.html'
    fields = '__all__'
    success_url = '/employee/'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list_url')
