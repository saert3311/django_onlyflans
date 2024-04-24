from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'frontpage'

urlpatterns = [
    path('', index_view, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('bienvenido', welcome_view, name='welcome'),
    path('acerca', about_view, name='about'),
    path('contacto', contact_view, name='contact'),
]