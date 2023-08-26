from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
