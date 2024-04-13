from django.urls import path
from .views import *

app_name = 'frontpage'

urlpatterns = [
    path('', index_view, name='index'),
]