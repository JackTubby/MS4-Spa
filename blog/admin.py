from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_url',
        'image',
    )


admin.site.register(Blog, BlogAdmin)
