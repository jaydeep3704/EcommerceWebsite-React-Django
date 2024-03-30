from django.contrib import admin
from .models import Category,Product,Color_Variant
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color_Variant)