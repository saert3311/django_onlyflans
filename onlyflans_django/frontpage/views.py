from operator import index
from django.views.generic import TemplateView

#tengo el presentimiento que mas adelante veremos vistas de clases asi que me adelanto un poco para
#no tener que hacer tantos cambios mas adelante

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Index'
        return context
    
index_view = IndexView.as_view()