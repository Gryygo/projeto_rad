from django.shortcuts import render, redirect
from django.contrib.auth import logout as LOGOUT


from apps.item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(stock__gt = 0)[0:6]
    categories = Category.objects.all()

    return render(
        request, 'core/index.html',
        {
        'categories': categories,
        'items': items,
        'user': ["{0}: {1}".format(field.name, getattr(request.user, field.name)) for field in request.user._meta.fields]
        }
    )

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout(request):
    LOGOUT(request)

    return redirect('/')