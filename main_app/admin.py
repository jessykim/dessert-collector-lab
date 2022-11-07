from django.contrib import admin
from .models import Dessert, Recipe

# Register your models here.
admin.site.register(Dessert)
admin.site.register(Recipe)