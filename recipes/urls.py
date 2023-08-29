from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_of_day, name='home'),
    path('recipes/', views.recipes_list, name='recipes'),
    path('recipes/<int:pk>/', views.recipes_detail, name='recipe_detail'),
    path('categories/', views.categories_list, name='categories'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('chefs/', views.chefs_page, name='chefs'),
    path('chefs/<int:pk>/', views.chef_detail, name='chef_detail')
]

