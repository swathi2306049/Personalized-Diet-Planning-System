from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Recipe
import datetime

def get_current_season():
    month = datetime.datetime.now().month
    if month in [3,4,5]: return 'summer'
    elif month in [6,7,8,9]: return 'monsoon'
    elif month in [10,11]: return 'spring'
    return 'winter'

def get_greeting():
    h = datetime.datetime.now().hour
    if h < 12: return 'Morning'
    elif h < 17: return 'Afternoon'
    return 'Evening'

@login_required
def dashboard(request):
    user = request.user
    health_filter = request.GET.get('health', '')
    meal_filter = request.GET.get('meal', '')
    diet_filter = request.GET.get('diet', '')
    search_query = request.GET.get('q', '')
    recipes = Recipe.objects.all()
    if health_filter: recipes = recipes.filter(health_tags=health_filter)
    if meal_filter: recipes = recipes.filter(meal_type=meal_filter)
    if diet_filter: recipes = recipes.filter(diet_type=diet_filter)
    if search_query: recipes = recipes.filter(title__icontains=search_query)
    user_health_recipes = []
    if user.health_condition and user.health_condition != 'none':
        user_health_recipes = Recipe.objects.filter(
            health_tags=user.health_condition)[:6]
    current_season = get_current_season()
    seasonal_recipes = Recipe.objects.filter(season=current_season)[:6]
    if not seasonal_recipes:
        seasonal_recipes = Recipe.objects.filter(is_featured=True)[:6]
    saved_ids = list(user.saved_recipes.values_list('id', flat=True))
    return render(request, 'recipes/dashboard.html', {
        'recipes': recipes, 'seasonal_recipes': seasonal_recipes,
        'user_health_recipes': user_health_recipes,
        'current_season': current_season,
        'health_filter': health_filter, 'meal_filter': meal_filter,
        'diet_filter': diet_filter, 'search_query': search_query,
        'saved_ids': saved_ids, 'greeting': get_greeting(),
    })

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    is_saved = request.user.saved_recipes.filter(pk=pk).exists()
    return render(request,'recipes/recipe_detail.html',
        {'recipe':recipe,'is_saved':is_saved})

@login_required
@require_POST
def toggle_save_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    user = request.user
    if user.saved_recipes.filter(pk=pk).exists():
        user.saved_recipes.remove(recipe)
        saved = False
    else:
        user.saved_recipes.add(recipe)
        saved = True
    return JsonResponse({'saved': saved})

@login_required
def saved_recipes(request):
    recipes = request.user.saved_recipes.all()
    saved_ids = list(request.user.saved_recipes.values_list('id', flat=True))
    return render(request,'recipes/saved_recipes.html',
        {'recipes':recipes,'saved_ids':saved_ids})
