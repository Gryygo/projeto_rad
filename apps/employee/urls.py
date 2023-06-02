from django.urls import path

from . import views

app_name = 'apps.employee'

urlpatterns = [
    path('', views.employees, name='employees'),
    
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('newuser/', views.new_user, name='new_user'),
]
