from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Dessert

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def desserts_index(request):
  desserts = Dessert.objects.all()
  return render(request, 'desserts/index.html', { 'desserts': desserts })

def desserts_detail(request, dessert_id):
  dessert = Dessert.objects.get(id=dessert_id)
  return render(request, 'desserts/detail.html', { 'dessert': dessert })

class DessertCreate(CreateView):
  model = Dessert
  fields = '__all__'