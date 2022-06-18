from django.contrib import admin
from django.db import models
from .models import Product,Variation,ReviewRating,ProductGallery
# Register your models here.

import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','varitation_category','varitaion_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','varitation_category','varitaion_value')

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)