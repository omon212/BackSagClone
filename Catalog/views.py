from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Count


class BrandView(APIView):
    def get(self, request, catalog_name):
        brands = GilamBrand.objects.all()
        result = []
        for brand in brands:
            status_counts = (
                GilamModel.objects
                .filter(gilam=brand)
                .values('status')
                .annotate(count=Count('status'))
                .order_by('-count')
            )
            most_common_status = status_counts[0]['status'].capitalize() if status_counts else None
            result.append({
                "id": brand.id,
                "name": brand.name,
                "img": brand.img.url if brand.img else None,
                "status": most_common_status
            })
        return Response(result, status=200)


class ModelView(APIView):
    def get(self, request, catalog_name, brand_name):
        models_map = {
            'gilam': (GilamBrand, GilamModel, GilamModelSerializer, 'gilam'),
            'kovrolin': (KovrolinBrand, KovrolinModel, KovrolinModelSerializer, 'kovrolin'),
            'gazon': (GazonBrand, GazonModel, GazonModelSerializer, 'gazon'),
            'metrli_yolak': (MetrliYolakBrand, MetrliYolakModel, MetrliYolakModelSerializer, 'yolak')
        }
        if catalog_name not in models_map:
            return Response({"error": "Bunday katalog topilmadi"}, status=404)
        brand_model, model_model, serializer_class, fk_field = models_map[catalog_name]
        try:
            brand = brand_model.objects.get(name=brand_name)
        except brand_model.DoesNotExist:
            return Response({"error": "Brand topilmadi"}, status=404)
        queryset = model_model.objects.filter(**{fk_field: brand})
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)
