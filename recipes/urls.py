from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', views.recipes_detail, name='recipe_detail'),
    path('category/', views.category_page, name='category'),
    # path('', views.chef, name='chef'),
]
