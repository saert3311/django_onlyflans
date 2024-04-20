from django.contrib import admin

# Register your models here.

from .models import Flan, Contact

admin.site.register([Flan, Contact])