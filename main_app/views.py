from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dessert, Spot
from .forms import RecipeForm

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
  recipe_form = RecipeForm()
  return render(request, 'desserts/detail.html', {
    'dessert': dessert, 
    'recipe_form': recipe_form 
  })

class DessertCreate(CreateView):
  model = Dessert
  fields = '__all__'

class DessertUpdate(UpdateView):
  model = Dessert
  fields = ['category', 'description']

class DessertDelete(DeleteView):
  model = Dessert
  success_url = '/desserts/'

def add_recipe(request, dessert_id):
  form = RecipeForm(request.POST)
  if form.is_valid():
    new_recipe = form.save(commit=False)
    new_recipe.dessert_id = dessert_id
    new_recipe.save()
  return redirect('desserts_detail', dessert_id=dessert_id)

class SpotCreate(CreateView):
  model = Spot
  fields = '__all__'

class SpotList(ListView):
  model = Spot

class SpotDetail(DetailView):
  model = Spot