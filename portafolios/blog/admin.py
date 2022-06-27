from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title"
    ]
    list_filter = [
        "author",
        "title"
    ]
    search_fields = [
        "author"
    ]

