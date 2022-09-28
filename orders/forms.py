from django import forms
from .models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class CartAddProductForm(forms.Form):
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

class CartDecreaseProductForm(CartAddProductForm):
    pass

Payment_CHICHES = (
    ("cash", "Cash on delivery"),
    ("credit_card", "Credit card"),
    ("debit_card", "Debit card"),
    ("paypal", "PayPal")
)

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "phone_number",
            "address",
            "address2",
            "region",
            "city",
            "paiment_method",
            "postal_code"
            ]
        widgets = {
            "first_name":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control",
                "Placeholder":"you@example.com"
            }),
            "phone_number":PhoneNumberPrefixWidget(attrs={
                "class":"form-control",
                "Placeholder":"722222222",
                "type":"tel"
            },initial="RO"),
            "address":forms.TextInput(attrs={
                "class":"form-control",
                "Placeholder":"1234 Main St",
            }),
            "address2":forms.TextInput(attrs={
                "class":"form-control",
                "Placeholder":"Apartment or suite",
            }),
            "region":forms.Select(attrs = {
                "id":"regions",
                "class":"form-select",
                "required":""
            }),
            "city":forms.Select(attrs = {
                "id":"towns",
                "class":"form-select",
                "disabled":"",
                "required":""
            }),
            "postal_code":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "paiment_method":forms.RadioSelect(attrs = {
                "class":"form-check-input",
                
            },choices=Payment_CHICHES ),
        }