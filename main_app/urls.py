from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('desserts/', views.desserts_index, name='desserts_index'),
  path('desserts/<int:dessert_id>/', views.desserts_detail, name='desserts_detail'),
  path('desserts/create/', views.DessertCreate.as_view(), name='desserts_create'),
  path('desserts/<int:pk>/update/', views.DessertUpdate.as_view(), name='desserts_update'),
  path('desserts/<int:pk>/delete/', views.DessertDelete.as_view(), name='desserts_delete'),
]
