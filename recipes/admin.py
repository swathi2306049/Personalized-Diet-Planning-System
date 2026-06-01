from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title','meal_type','diet_type','health_tags',
        'season','calories','is_featured']
    list_filter = ['meal_type','diet_type','health_tags','season','is_featured']
    search_fields = ['title','description']
    list_editable = ['is_featured']
