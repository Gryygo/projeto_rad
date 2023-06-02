from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Employee

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSES_CHECK = 'h-6 w-6 text-teal-500'

class NewEmployeeForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=True)
        self.fields['user'].widget.attrs.update({
            'class': INPUT_CLASSES
        })

    class Meta:
        model = Employee
        fields = ('user', 'can_create', 'can_edit', 'can_delete', 'can_create_user', 'can_edit_user', 'can_delete_user')
        widgets = {
            'user': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_edit': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_delete': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_create_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_edit_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_delete_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            })
        }

class EditEmployeeForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=True)
        self.fields['user'].widget.attrs.update({
            'class': INPUT_CLASSES
        })

    class Meta:
        model = Employee
        fields = ('user', 'can_create', 'can_edit', 'can_delete', 'can_create_user', 'can_edit_user', 'can_delete_user')
        widgets = {
            'user': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'can_create': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_edit': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_delete': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_create_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_edit_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            }),
            'can_delete_user': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES_CHECK
            })
        }

class NewUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['is_staff'] = True
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Insert username',
        'class': INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Insert email',
        'class': INPUT_CLASSES,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Insert password',
        'class': INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': INPUT_CLASSES
    }))

    is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': INPUT_CLASSES_CHECK,
        'checked': True
    }), initial=True)