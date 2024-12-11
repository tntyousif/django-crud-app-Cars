from django.contrib import admin
from .models import Car, Filling, Modification

# Register your models here.

admin.site.register(Car)

admin.site.register(Filling)

admin.site.register(Modification)