from django.forms import ModelForm, widgets
from store.models import Product, Review
from django import forms


class GiveRatingForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'rating': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
