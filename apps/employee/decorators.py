import functools
from django.shortcuts import redirect
from django.contrib import messages

def can_see_employee(view_func, redirect_url="apps.core:index"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee'):
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to see employees")
        return redirect(redirect_url)
    return wrapper

def can_create_employee(view_func, redirect_url="apps.employee:employees"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_create_user:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to create employees")
        return redirect(redirect_url)
    return wrapper

def can_edit_employee(view_func, redirect_url="apps.employee:employees"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_edit_user:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to edit employees")
        return redirect(redirect_url)
    return wrapper

def can_delete_employee(view_func, redirect_url="apps.employee:employees"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_delete_user:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to delete employees")
        return redirect(redirect_url)
    return wrapper