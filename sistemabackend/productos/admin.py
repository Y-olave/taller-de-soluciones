from django.contrib import admin

# Register your models here.

from .models import producto, usuario

admin.site.register(producto)
admin.site.register(usuario)

