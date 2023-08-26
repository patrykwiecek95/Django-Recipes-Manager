from django.contrib import admin
from .models import Ingredient,Category,Chef,Recipe


admin.site.register(Ingredient)

admin.site.register(Category)

admin.site.register(Chef)

admin.site.register(Recipe)