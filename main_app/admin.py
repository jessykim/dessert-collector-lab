from django.contrib import admin
from .models import Dessert, Recipe, Spot

# Register your models here.
admin.site.register(Dessert)
admin.site.register(Recipe)
admin.site.register(Spot)