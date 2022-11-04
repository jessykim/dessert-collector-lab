from django.shortcuts import render
from .models import Dessert

# class Dessert:
#   def __init__(self, name, category, description):
#     self.name = name
#     self.category = category
#     self.description = description

# desserts = [
#   Dessert('Tiramisu', 'cake', 'Coffee-flavoured Italian dessert made of ladyfingers dipped in coffee, layered with sweet cream, mascarpone cheese and topped with cocoa.'),
#   Dessert('Bubble Tea', 'beverage', 'Tea-based drink, served cold or hot, with the option to add tapioca pearls as a topping.'),
#   Dessert('Pistachio Muffin', 'pastry', 'The perfect breakfast muffin that can easily be baked used pistachio pudding mix.'),
#   Dessert('Strawberry Cheesecake', 'cake', 'A thick and creamy dessert cake with a thin layer of crust on the bottom, topped with fresh strawberries.'),
#   Dessert('Oreo McFlurry', 'ice cream', 'The best midnight snack on a summer night, especially if you love oreos.'),
#   Dessert('Chocolate Croissant', 'pastry', 'A buttery, flaky, French viennoiserie pastry with the perfect amount of chococlate in every bite.')
# ]

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