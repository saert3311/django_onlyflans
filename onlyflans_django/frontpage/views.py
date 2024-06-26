from django.views.generic import ListView, TemplateView, CreateView
from django.contrib import messages
from .models import Flan, Contact
from .forms import ContactForm

#tengo el presentimiento que mas adelante veremos vistas de clases asi que me adelanto un poco para
#no tener que hacer tantos cambios mas adelante y que vamos a ir trabajando sobre el mismo proyecto

class IndexView(ListView):
    template_name = 'index.html'
    model = Flan
    context_object_name = 'flans' #nombre con el que se va a pasar la lista de objetos a la plantilla

    def get_queryset(self):
        queryset = super().get_queryset()
        #limitamos a solo mostrar los flanes publicos
        queryset = queryset.filter(is_private=False)
        return queryset

    #sobreescribo context_data para agregarle informacion, como en el dict en las vistas en funciones
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Inicio'
        return context
    
index_view = IndexView.as_view()

class WelcomeView(ListView):
    template_name = 'index.html' #por ahora usemos la misma plantilla que en index
    model = Flan
    context_object_name = 'flans' #nombre con el que se va a pasar la lista de objetos a la plantilla

    def get_queryset(self):
        queryset = super().get_queryset()
        #limitamos a solo mostrar los flanes publicos
        queryset = queryset.filter(is_private=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Bienvenido'
        return context
    
welcome_view = WelcomeView.as_view()

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Acerca de'
        return context
    
about_view = AboutView.as_view()

class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Mensaje Enviado!")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Contacto'
        return context
    
contact_view = ContactView.as_view()