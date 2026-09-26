from re import search
from django.contrib import admin
from .models import Product, Color, Yaddas, ProductImage, ProductProperty


admin.site.register([Color, Yaddas, ProductImage, ProductProperty])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount', 'discount_price']
    list_display_links = ['id', 'name']
    list_filter = ['yaddas', 'color']
    search_fields = ['name']
    ordering = ['-id']
    filter_horizontal = ['yaddas', 'color']
