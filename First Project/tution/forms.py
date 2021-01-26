from django import forms


class  ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    phone = forms.CharField(max_length=100, label="Your Phone")
    message = forms.CharField(max_length=100, label="Your Message")