from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('desserts/', views.desserts_index, name='desserts_index'),
  path('desserts/<int:dessert_id>/', views.desserts_detail, name='desserts_detail'),
  path('desserts/create/', views.DessertCreate.as_view(), name='desserts_create'),
  path('desserts/<int:pk>/update/', views.DessertUpdate.as_view(), name='desserts_update'),
  path('desserts/<int:pk>/delete/', views.DessertDelete.as_view(), name='desserts_delete'),
  path('desserts/<int:dessert_id>/add_recipe/', views.add_recipe, name='add_recipe'),
  path('spots/create/', views.SpotCreate.as_view(), name='spots_create'),
  path('spots/<int:pk>/', views.SpotDetail.as_view(), name='spots_detail'),
  path('spots/', views.SpotList.as_view(), name='spots_index'),
  path('spots/<int:pk>/update/', views.SpotUpdate.as_view(), name='spots_update'),
  path('spots/<int:pk>/delete/', views.SpotDelete.as_view(), name='spots_delete'),
  path('desserts/<int:dessert_id>/assoc_spot/<int:spot_id>/', views.assoc_spot, name='assoc_spot'),
  path('accounts/signup/', views.signup, name='signup')
]
