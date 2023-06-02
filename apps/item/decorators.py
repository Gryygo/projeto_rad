import functools
from django.shortcuts import redirect
from django.contrib import messages

def can_create_items(view_func, redirect_url="apps.core:index"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_create:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to create items")
        return redirect(redirect_url)
    return wrapper

def can_edit_items(view_func, redirect_url="apps.core:index"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_edit:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to edit items")
        return redirect(redirect_url)
    return wrapper

def can_delete_items(view_func, redirect_url="apps.core:index"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'employee') and request.user.employee.can_delete:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You don't have permission to delete items")
        return redirect(redirect_url)
    return wrapper