from django.contrib import admin
from django.utils.html import format_html
from .models import (
    GilamBrand, GilamModel,
    KovrolinBrand, KovrolinModel,
    GazonBrand, GazonModel,
    MetrliYolakBrand, MetrliYolakModel
)


@admin.register(GilamBrand)
class GilamBrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview_image", "model_count")
    search_fields = ("name",)
    ordering = ("name",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"

    def model_count(self, obj):
        return obj.models.count()

    model_count.short_description = "Models"


@admin.register(GilamModel)
class GilamModelAdmin(admin.ModelAdmin):
    list_display = ("id", "gilam", "gilam_mark", "color", "size", "style", "price", "status", "preview_image")
    list_filter = ("room", "color", "size", "style", "status")
    search_fields = ("gilam__name", "gilam_mark", "color", "size")
    ordering = ("gilam", "gilam_mark")
    autocomplete_fields = ("gilam",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"


@admin.register(KovrolinBrand)
class KovrolinBrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview_image", "model_count")
    search_fields = ("name",)
    ordering = ("name",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"

    def model_count(self, obj):
        return obj.models.count()

    model_count.short_description = "Models"


@admin.register(KovrolinModel)
class KovrolinModelAdmin(admin.ModelAdmin):
    list_display = ("id", "kovrolin", "kovrolin_mark", "color", "size", "price", "status", "preview_image")
    list_filter = ("room", "color", "size", "status")
    search_fields = ("kovrolin__name", "kovrolin_mark", "color", "size")
    ordering = ("kovrolin", "kovrolin_mark")
    autocomplete_fields = ("kovrolin",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"


@admin.register(GazonBrand)
class GazonBrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview_image", "model_count")
    search_fields = ("name",)
    ordering = ("name",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"

    def model_count(self, obj):
        return obj.models.count()

    model_count.short_description = "Models"


@admin.register(GazonModel)
class GazonModelAdmin(admin.ModelAdmin):
    list_display = ("id", "gazon", "gazon_mark", "color", "size", "price", "status", "preview_image")
    list_filter = ("room", "color", "size", "status")
    search_fields = ("gazon__name", "gazon_mark", "color", "size")
    ordering = ("gazon", "gazon_mark")
    autocomplete_fields = ("gazon",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"


@admin.register(MetrliYolakBrand)
class MetrliYolakBrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview_image", "model_count")
    search_fields = ("name",)
    ordering = ("name",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"

    def model_count(self, obj):
        return obj.models.count()

    model_count.short_description = "Models"


@admin.register(MetrliYolakModel)
class MetrliYolakModelAdmin(admin.ModelAdmin):
    list_display = ("id", "yolak", "yolak_mark", "color", "size", "price", "status", "preview_image")
    list_filter = ("room", "color", "size", "status")
    search_fields = ("yolak__name", "yolak_mark", "color", "size")
    ordering = ("yolak", "yolak_mark")
    autocomplete_fields = ("yolak",)

    def preview_image(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return format_html('<img src="{}" width="80" height="50" '
                               'style="object-fit:cover;border-radius:6px;" />', obj.img.url)
        return "—"

    preview_image.short_description = "Image"
