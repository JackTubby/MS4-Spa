from django.contrib import admin
from .models import Treatment, Category, Rating


class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'amount',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
    )


admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
