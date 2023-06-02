from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Employee
from .forms import NewEmployeeForm, EditEmployeeForm, NewUserForm
from .decorators import can_create_employee, can_delete_employee, can_edit_employee, can_see_employee

@login_required
@can_see_employee
def employees(request):
    messages.info(request, "You don't have permission to create items")
    query = request.GET.get('query', '')
    employees = Employee.objects.all()

    if query:
        employees = employees.filter(Q(user__username__icontains=query))

    return render(request, 'employee/employees.html', {
        'employees': employees,
        'query': query,
        'messages': messages
    })

@login_required
@can_create_employee
def new(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            employee = form.save(commit=False)
            employee.created_by = request.user
            employee.save()

            return redirect('apps.employee:employees')
    else:
        form = NewEmployeeForm()

    return render(request, 'employee/form.html', {
        'form': form,
        'title': 'New employee'
    })

@login_required
@can_edit_employee
def edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditEmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()

            return redirect('apps.employee:employees')
    else:
        form = EditEmployeeForm(instance=employee)

    return render(request, 'employee/form.html', {
        'form': form,
        'title': 'Edit employee'
    })

@login_required
@can_delete_employee
def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk, created_by=request.user)
    employee.delete()

    return redirect('apps.employee:employees')

@login_required
@can_create_employee
def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/employees/')
    else:
        form = NewUserForm()

    return render(request, 'employee/create_user.html', {
        'form': form
    })
