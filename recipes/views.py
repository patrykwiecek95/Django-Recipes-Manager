from django.shortcuts import render
from .models import Recipe
from django.shortcuts import get_object_or_404


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def recipes_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
