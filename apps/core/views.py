from django.shortcuts import render, redirect
from django.contrib.auth import logout as LOGOUT
from django.contrib.auth.decorators import login_required


from apps.item.models import Category, Item
from .forms import SignupForm

@login_required
def index(request):
    items = Item.objects.filter(stock__gt = 0)[0:10]
    categories = Category.objects.all()

    return render(
        request, 'core/index.html',
        {
        'categories': categories,
        'items': items,
        'user': request.user
        }
    )
    
@login_required
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
    
@login_required
def logout(request):
    LOGOUT(request)

    return redirect('/')