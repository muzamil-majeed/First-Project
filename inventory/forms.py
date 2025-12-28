from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        labels = {
            "name":"Your Name",
            "phone":"Your Phone Number",
            "message":"Your Message"
        }