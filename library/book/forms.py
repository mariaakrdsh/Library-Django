from django import forms
from author.models import Author
from .models import Book
from order.models import Order

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic', 'books')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'books': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'year_of_publication', 'date_of_issue')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'count' : forms.NumberInput(attrs={'class':'form-control'}),
            'year_of_publication': forms.NumberInput(attrs={'class':'form-control'}),
            'date_of_issue': forms.DateInput(
                    format=('%Y-%m-%d'),attrs={'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('book', 'user')

