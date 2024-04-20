from django import forms


class ContactForm(forms.Form):
    customer_name = forms.CharField(label='Nombre', max_length=64)
    customer_email = forms.EmailField(label='Email')
    customer_message = forms.CharField(label='Mensaje')