from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #Heredamos de este tambien para que solo usuarios logueados puedan acceder 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Flan, Contact
from .forms import ContactForm, AuthForm
from django.shortcuts import redirect

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

class ListContacts(LoginRequiredMixin, ListView):
    template_name = 'list_contacts.html'
    model = Contact
    context_object_name = 'contacts'
    login_url = "/login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Contactos recibidos'
        return context
    
list_contacts_view = ListContacts.as_view()

class WelcomeView(LoginRequiredMixin, ListView):
    template_name = 'welcome.html' #por ahora usemos la misma plantilla que en index
    model = Flan
    context_object_name = 'flans' #nombre con el que se va a pasar la lista de objetos a la plantilla
    login_url = "/login" #redirigir a esta url si no esta logueado
    redirect_field_name = "redirect_to"

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

class Login(LoginView):
    template_name = 'account/login.html'
    authentication_form = AuthForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Login'
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.POST.get('remember'):
                    request.session.set_expiry(0)
                messages.add_message(self.request, messages.SUCCESS, f'Bienvenido! ${self.request.user.first_name}')
                return redirect('/')
            else:
                return super().post(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

login_view = Login.as_view()

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Sesion cerrada!')
    return redirect('/')