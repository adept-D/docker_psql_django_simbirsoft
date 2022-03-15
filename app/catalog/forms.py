from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import NoteUser
from django.core.exceptions import ValidationError
import uuid


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'width: 100%',
    }))

    #email
    username = forms.EmailField(label='Email', widget= forms.EmailInput(attrs={
        'class': 'form-control',
        'style': 'width: 100%',
    }))
    


def validate_email(value):
    if NoteUser.objects.filter(email = value).exists():
        raise ValidationError(( f"Email: {value} уже зарегистрирован"),params = {'value':value})
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', validators=[validate_email], widget= forms.EmailInput(attrs={
        'class': 'form-control',
        'style': 'width: 100%',
    }))
    password1 = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'width: 100%',
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'width: 100%',
    }))

    class Meta:
        model =  NoteUser  #User
        fields = ('email', 'password1', 'password2') #'username', 

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields= ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'form-control',
                'style':'''
                        font-size: 16px; 
                        max-height: 70vh; 
                        min-height: 300px; 
                        min-width: 700px;
                        max-width: 90%;
                        width: 100%;
                        height: 100%; 
                        ''',
                'placeholder': 'Введите текст...',
            }),
        }
#                     