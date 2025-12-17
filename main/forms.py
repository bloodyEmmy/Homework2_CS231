from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'is_done', 'category']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'deadline': 'Дедлайн',
            'is_done': 'Выполнено',
            'category': 'Категория',
        }
        help_texts = {
            'deadline': 'Формат: ДД.ММ.ГГГГ (например, 25.12.2024)',
        }
        widgets = {
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'ДД.ММ.ГГГГ'
            }),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации с русскими полями"""
    username = forms.CharField(
        label='Имя пользователя',
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_',
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    password1 = forms.CharField(
        label='Пароль',
        help_text='Минимум 8 символов. Не должен быть слишком простым.',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        help_text='Введите тот же пароль для подтверждения',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'})
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')