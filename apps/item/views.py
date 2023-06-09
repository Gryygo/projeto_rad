from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Sum

from .models import Item, Category
from .forms import NewItemForm, EditItemForm
from .decorators import can_create_items, can_delete_items, can_edit_items

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(stock__gt = 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, stock__gt = 0).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',
        {
        'item': item,
        'related_items': related_items
        }
    )

@login_required
@can_create_items
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('apps.item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item'
    })

@login_required
@can_edit_items
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('apps.item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item'
    })

@login_required
@can_delete_items
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('apps.dashboard:index')

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    user_profile = request.user.userprofile
    user_profile.cart.add(item)
    return redirect('apps.item:detail', item_id)

@login_required
def view_cart(request):
    user_profile = request.user.userprofile
    cart_items = user_profile.cart.all()
    total_price = cart_items.aggregate(total_price=Sum('price'))['total_price']
    return render(request, 'item/cart.html', {
        'items': cart_items,
        'total_price': total_price
    })

@login_required
def checkout(request):
    user_profile = request.user.userprofile
    cart_items = user_profile.cart.all()

    for item in cart_items:
        item.stock -= 1
        item.save()

    user_profile.cart.clear()

    return redirect('apps.core:index')

@login_required
def clear_cart(request):
    user_profile = request.user.userprofile
    user_profile.cart.clear()

    return redirect('apps.core:index')