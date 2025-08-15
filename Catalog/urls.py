from django.urls import path
from .views import BrandView, ModelView

urlpatterns = [
    path('<str:catalog_name>/', BrandView.as_view(), name='brand-list'),
    path('<str:brand_name>/<str:catalog_name>/', ModelView.as_view(), name='model-list'),
]
