from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'message': 'Mensaje',
        }
        error_messages = {
            'name': {
                'required': 'Por favor escribe tu nombre',
            },
            'email': {
                'required': 'Por favor escribe tu correo',
            },
            'message': {
                'required': 'Por favor escribe tu mensaje',
            },
        }
        widgets = {
            'message': Textarea(attrs={'rows': 5}),
        }