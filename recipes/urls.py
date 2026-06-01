from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/save/', views.toggle_save_recipe, name='toggle_save'),
    path('saved/', views.saved_recipes, name='saved_recipes'),
]
