"""imageuploader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Create a router and register our viewsets with it.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from catalogue.views import CatalogueImageViewSet, CatalogueViewSet

router = DefaultRouter()
router.register(r'autocomplete', CatalogueViewSet, basename="autocomplete")
router.register(r'images', CatalogueImageViewSet, basename="images")

# The API URLs are now determined automatically by the router.


@api_view()
def root(request):
    return Response({
        "auto-complete": request.build_absolute_uri('/api/v1/catalogue/autocomplete'),
        "images": request.build_absolute_uri('/api/v1/catalogue/images/'),
    })


urlpatterns = [
    path('api/v1/', root),
    path('api/v1/catalogue/', include(router.urls)),
    path('', admin.site.urls),
]



