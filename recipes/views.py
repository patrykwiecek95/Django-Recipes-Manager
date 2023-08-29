from django.shortcuts import render
from .models import Recipe, Category, Chef
from django.shortcuts import get_object_or_404
import random


def recipe_of_day(request):
    recipes_data = Recipe.objects.all()
    count = len(recipes_data)
    random_index = random.randint(0, count - 1)
    random_recipe = recipes_data[random_index]
    return render(request, 'recipes/recipe_of_day.html', {'random_recipe': random_recipe, "index": random_index + 1})


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipes_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})


def category_detail(request, pk):
    category_recipes = get_object_or_404(Category, pk=pk)
    recipes = Recipe.objects.filter(categories=category_recipes)
    return render(request, 'categories/category_detail.html', {'category': category_recipes, 'recipes': recipes})


def chefs_page(request):
    chefs = Chef.objects.all()
    return render(request, 'chefs/chefs.html', {'chefs': chefs})


def chef_detail(request, pk):
    chef = get_object_or_404(Chef, pk=pk)
    recipes = Recipe.objects.filter(chef=chef)
    return render(request, 'chefs/chef_detail.html', {"chef": chef, "recipes": recipes})
