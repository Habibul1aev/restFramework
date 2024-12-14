from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, Tags

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'get_image')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'price')
    readonly_fields = ('id', 'created_date', 'update_date', 'get_full_image')

    @admin.display()
    def get_full_image(self, prod:Product):
        return mark_safe(f'<img src={prod.image.url} width="50%" />')

    @admin.display()
    def get_image(self, prod:Product):
        return mark_safe(f'<img src={prod.image.url} width="150px" />')



admin.site.register(Category)
admin.site.register(Tags)