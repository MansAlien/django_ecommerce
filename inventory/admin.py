from django.contrib import admin
from .models import Cateogry, Product

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cateogry, CategoryAdmin)
admin.site.register(Product)

