from django.shortcuts import render

from rest_framework import viewsets, serializers

from catalogue.models import Catalogue, CatalogueImage


class CatalogueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalogue
        fields = ('id', 'name', 'sku_id')


class CatalogueImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatalogueImage
        fields = (
            'id', 'sku_id', 'image_01', 'image_02', 'image_03', 'image_04',
            'image_05', 'image_06', 'image_07', 'image_08',
        )


class CatalogueViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list` and `retrieve` actions.
    """
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer

    def filter_queryset(self, queryset):
        search_term = self.request.GET.get('q')
        if search_term:
            return queryset.filter(name__icontains=search_term)
        return queryset


class CatalogueImageViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list`, `retrieve`, `create`, `update`, `partial_update` and `destroy` actions.
    """
    queryset = CatalogueImage.objects.all()
    serializer_class = CatalogueImageSerializer

