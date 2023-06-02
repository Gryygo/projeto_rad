from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Employee

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('user', 'can_create', 'can_edit', 'can_delete', 'can_create_user', 'can_edit_user', 'can_delete_user')
        widgets = {
            'user': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_edit': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_delete': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_edit_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_delete_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('user', 'can_create', 'can_edit', 'can_delete', 'can_create_user', 'can_edit_user', 'can_delete_user')
        widgets = {
            'user': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_edit': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_delete': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_edit_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'can_delete_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Insert username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Insert email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Insert password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))