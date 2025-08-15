from django.db import models
from .choices import *


class RoomModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class ColorModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Shape(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class StyleModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class CategoriesModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class CategoryBrand(models.Model):
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='brands_img/')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Yangi')

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    brand = models.ForeignKey(CategoryBrand, on_delete=models.CASCADE, related_name="brands")
    mark = models.CharField(max_length=4)
    img = models.ImageField(upload_to='marks_img/')
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name="rooms")
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE, related_name="colors")
    style = models.ForeignKey(StyleModel, on_delete=models.CASCADE, related_name="styles")
    price = models.CharField(max_length=128)
    discount = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Yangi')

    def __str__(self):
        return f"{self.brand.name} - {self.mark} - {self.color}"


class SizeModel(models.Model):
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    width = models.CharField(max_length=32)
    height = models.CharField(max_length=32)
    price = models.CharField(max_length=64)
    discount = models.CharField(max_length=64, blank=True, null=True)
    model = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.width} X {self.height}"


class CharacterModel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class CharacterTitle(models.Model):
    character = models.ForeignKey(CharacterModel, on_delete=models.CASCADE)
    model = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    detail = models.CharField(max_length=128)

    def __str__(self):
        return self.title
