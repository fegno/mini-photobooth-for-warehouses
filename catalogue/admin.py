from django.contrib import admin

# Register your models here.
from catalogue.models import CatalogueImage, Catalogue

admin.site.register(Catalogue)
admin.site.register(CatalogueImage)
