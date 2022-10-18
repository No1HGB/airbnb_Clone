from tabnanny import verbose
from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "kind",
    )
    list_filter = ("kind",)

    class Meta:
        verbose_name_plural = "카테고리"
