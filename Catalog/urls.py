from django.urls import path
from .views import BrandListView, ModelListView

urlpatterns = [
    path('<str:catalog_name>/', BrandListView.as_view(), name='brand-list'),
    path('<str:brand_name>/<str:catalog_name>/', ModelListView.as_view(), name='model-list'),
]
