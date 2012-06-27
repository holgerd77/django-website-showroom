from website_showroom.models import Category, Website
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color', 'active_color')
    ordering = ['order']
    prepopulated_fields = {"url_name": ("name",)}

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'country', 'url')
    list_filter = ['category']
    search_fields = ['title']
    ordering = ['category', 'order']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Website, WebsiteAdmin)
