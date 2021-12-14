from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('position/', PositionListView.as_view(), name='position_list_url'),
    path('position/<int:pk>/delete', PositionDeleteView.as_view(), name='position_delete_url'),
    path('position/create/', PositionCreateView.as_view(), name='position_create_url'),
    path('department/', DepartmentListView.as_view(), name='department_list_url'),
    path('department/<int:pk>/delete', DepartmentDeleteView.as_view(), name='department_delete_url'),
    path('department/create/', DepartmentCreateView.as_view(), name='department_create_url'),
    path('employee/', EmployeeListView.as_view(), name='employee_list_url'),
    path('employee/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee_delete_url'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create_url'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail_url'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update_url'),

]
