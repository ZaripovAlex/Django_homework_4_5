from django import forms
from .models import Client, Items, Order


class EditItemsForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Items.objects.all(),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control'}),
                                  label="Товар")
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Наименование товара'}),
        label="Наименование")
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}),
        label='Описание товара:')
    price = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'min': 1}),
        label='Цена:')
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'min': 1}),
        label='Количество товара')


class LoadImageForProduct(forms.Form):
    item = forms.ModelChoiceField(queryset=Items.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Товар:')
    image = forms.ImageField(widget=forms.FileInput())
