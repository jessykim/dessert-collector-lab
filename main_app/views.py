from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dessert, Spot
from .forms import RecipeForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def desserts_index(request):
  desserts = Dessert.objects.filter(user=request.user)
  return render(request, 'desserts/index.html', { 'desserts': desserts })

@login_required
def desserts_detail(request, dessert_id):
  dessert = Dessert.objects.get(id=dessert_id)
  spots_dessert_doesnt_list = Spot.objects.exclude(id__in = dessert.spots.all().values_list('id'))
  recipe_form = RecipeForm()
  return render(request, 'desserts/detail.html', {
    'dessert': dessert, 
    'recipe_form': recipe_form,
    'spots': spots_dessert_doesnt_list 
  })

class DessertCreate(LoginRequiredMixin, CreateView):
  model = Dessert
  fields = ['name', 'category', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DessertUpdate(LoginRequiredMixin, UpdateView):
  model = Dessert
  fields = ['category', 'description']

class DessertDelete(LoginRequiredMixin, DeleteView):
  model = Dessert
  success_url = '/desserts/'

@login_required
def add_recipe(request, dessert_id):
  form = RecipeForm(request.POST)
  if form.is_valid():
    new_recipe = form.save(commit=False)
    new_recipe.dessert_id = dessert_id
    new_recipe.save()
  return redirect('desserts_detail', dessert_id=dessert_id)

class SpotCreate(LoginRequiredMixin, CreateView):
  model = Spot
  fields = '__all__'

class SpotList(LoginRequiredMixin, ListView):
  model = Spot

class SpotDetail(LoginRequiredMixin, DetailView):
  model = Spot

class SpotUpdate(LoginRequiredMixin, UpdateView):
  model = Spot
  fields = '__all__'

class SpotDelete(LoginRequiredMixin, DeleteView):
  model = Spot
  success_url = '/spots/'

@login_required
def assoc_spot(request, dessert_id, spot_id):
  Dessert.objects.get(id=dessert_id).spots.add(spot_id)
  return redirect('desserts_detail', dessert_id=dessert_id)

@login_required
def remove_spot(request, dessert_id, spot_id):
  Dessert.objects.get(id=dessert_id).spots.remove(spot_id)
  return redirect('desserts_detail', dessert_id=dessert_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('desserts_index')
    else:
      error_message = 'Invalid sign up - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)