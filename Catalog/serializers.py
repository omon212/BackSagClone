from rest_framework import serializers
from .models import (
    GilamBrand, KovrolinBrand, GazonBrand, MetrliYolakBrand,
    GilamModel, KovrolinModel, GazonModel, MetrliYolakModel
)


class GilamBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GilamBrand
        fields = '__all__'


class KovrolinBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = KovrolinBrand
        fields = '__all__'


class GazonBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GazonBrand
        fields = '__all__'


class MetrliYolakBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetrliYolakBrand
        fields = '__all__'


class GilamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GilamModel
        fields = '__all__'


class KovrolinModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KovrolinModel
        fields = '__all__'


class GazonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GazonModel
        fields = '__all__'


class MetrliYolakModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetrliYolakModel
        fields = '__all__'
