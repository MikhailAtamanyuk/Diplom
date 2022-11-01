from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput())
    phone = forms.CharField(max_length=200, widget=forms.TextInput())
    country = forms.CharField(max_length=200, widget=forms.TextInput())
    city = forms.CharField(max_length=200, widget=forms.TextInput())