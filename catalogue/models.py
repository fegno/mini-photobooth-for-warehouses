from django.db import models


class Catalogue(models.Model):
    name = models.CharField(max_length=32)
    sku_id = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class CatalogueImage(models.Model):
    sku_id = models.CharField(max_length=32)
    image_01 = models.ImageField()
    image_02 = models.ImageField(null=True, blank=True)
    image_03 = models.ImageField(null=True, blank=True)
    image_04 = models.ImageField(null=True, blank=True)
    image_05 = models.ImageField(null=True, blank=True)
    image_06 = models.ImageField(null=True, blank=True)
    image_07 = models.ImageField(null=True, blank=True)
    image_08 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sku_id

