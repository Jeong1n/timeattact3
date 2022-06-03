from django.db import models


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    def __str__(self):
        return self.drink_name

    drink_name = models.CharField(max_length=256)
    drink_category = models.CharField(max_length=256)
    nutrition = models.CharField(max_length=256)
    allergy = models.CharField(max_length=256)


class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=256)
    category_drinks = models.ManyToManyField(Drink)
