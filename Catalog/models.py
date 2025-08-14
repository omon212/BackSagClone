from django.db import models
from .choices import *


class GilamBrand(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='gilam_brand/')

    def __str__(self):
        return self.name


class GilamModel(models.Model):
    gilam = models.ForeignKey(GilamBrand, on_delete=models.CASCADE, related_name="models")
    gilam_mark = models.CharField(max_length=4)
    img = models.ImageField(upload_to='gilam_model/')
    room = models.CharField(max_length=50, choices=ROOM_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    price = models.CharField(max_length=128)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='yangilik')

    def __str__(self):
        return f"{self.gilam.name} - {self.color} - {self.size}"


class KovrolinBrand(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='kovrolin_brand/')

    def __str__(self):
        return self.name


class KovrolinModel(models.Model):
    kovrolin = models.ForeignKey(KovrolinBrand, on_delete=models.CASCADE, related_name="models")
    kovrolin_mark = models.CharField(max_length=4)
    img = models.ImageField(upload_to='kovrolin_model/')
    room = models.CharField(max_length=50, choices=ROOM_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    price = models.CharField(max_length=128)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='yangilik')

    def __str__(self):
        return f"{self.kovrolin.name} - {self.color} - {self.size}"


class GazonBrand(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='gazon_brand/')

    def __str__(self):
        return self.name


class GazonModel(models.Model):
    gazon = models.ForeignKey(GazonBrand, on_delete=models.CASCADE, related_name="models")
    gazon_mark = models.CharField(max_length=4)
    img = models.ImageField(upload_to='gazon_model/')
    room = models.CharField(max_length=50, choices=ROOM_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    price = models.CharField(max_length=128)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='yangilik')

    def __str__(self):
        return f"{self.gazon.name} - {self.color} - {self.size}"


class MetrliYolakBrand(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='metrliyolak_brand/')

    def __str__(self):
        return self.name


class MetrliYolakModel(models.Model):
    yolak = models.ForeignKey(MetrliYolakBrand, on_delete=models.CASCADE, related_name="models")
    yolak_mark = models.CharField(max_length=4)
    img = models.ImageField(upload_to='metrliyolak_model/')
    room = models.CharField(max_length=50, choices=ROOM_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    price = models.CharField(max_length=128)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='yangilik')

    def __str__(self):
        return f"{self.yolak.name} - {self.color} - {self.size}"
