from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class BrandListView(APIView):
    def get(self, request, catalog_name):
        catalogs_map = {
            'gilam': (GilamBrand, GilamBrandSerializer),
            'kovrolin': (KovrolinBrand, KovrolinBrandSerializer),
            'gazon': (GazonBrand, GazonBrandSerializer),
            'metrli_yolak': (MetrliYolakBrand, MetrliYolakBrandSerializer)
        }

        if catalog_name not in catalogs_map:
            return Response({"error": "Bunday katalog topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        model_class, serializer_class = catalogs_map[catalog_name]
        queryset = model_class.objects.all()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ModelListView(APIView):
    def get(self, request, catalog_name, brand_name):
        models_map = {
            'gilam': (GilamBrand, GilamModel, GilamModelSerializer, 'gilam'),
            'kovrolin': (KovrolinBrand, KovrolinModel, KovrolinModelSerializer, 'kovrolin'),
            'gazon': (GazonBrand, GazonModel, GazonModelSerializer, 'gazon'),
            'metrli_yolak': (MetrliYolakBrand, MetrliYolakModel, MetrliYolakModelSerializer, 'yolak')
        }

        if catalog_name not in models_map:
            return Response({"error": "Bunday katalog topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        brand_model, model_model, serializer_class, fk_field = models_map[catalog_name]

        try:
            brand = brand_model.objects.get(name=brand_name)
        except brand_model.DoesNotExist:
            return Response({"error": "Brand topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        queryset = model_model.objects.filter(**{fk_field: brand})
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
