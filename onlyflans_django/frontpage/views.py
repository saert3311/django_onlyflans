from operator import index
from django.views.generic import TemplateView

#tengo el presentimiento que mas adelante veremos vistas de clases asi que me adelanto un poco para
#no tener que hacer tantos cambios mas adelante y que vamos a ir trabajando sobre el mismo proyecto

class IndexView(TemplateView):
    template_name = 'index.html'
    #sobreescribo context_data para agregarle informacion, como en el dict en las vistas en funciones
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Inicio'
        return context
    
index_view = IndexView.as_view()

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

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