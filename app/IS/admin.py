from django.contrib import admin
from .models import Product
from django.contrib.auth.models import *
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(auth.models.User)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['description_s', 'image_front']
    
admin.site.register(Product, ProductAdmin)