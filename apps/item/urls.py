from django.urls import path

from . import views

app_name = 'apps.item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/clear', views.clear_cart, name='clear_cart'),
     path('checkout/', views.checkout, name='checkout'),
]
