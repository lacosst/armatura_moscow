from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fio', 'phone_number', 'email']
        labels = {'fio': 'ФИО', 'phone_number': 'Номер телефона', 'email': 'Email'}
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control',
                                          'type': 'text',
                                          'placeholder': 'Иванов Иван Иванович'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'type': 'tel',
                                                   # 'pattern': "[0-9]{3}-[0-9]{3}-[0-9]{4}",
                                                   'placeholder': '+7 (123) 456-78-90'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'type': 'email',
                                            'placeholder': 'youmail@mail.ru'})
        }
