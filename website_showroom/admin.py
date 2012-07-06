from website_showroom.models import Edition, Category, Website, EditionCategory, EditionWebsite
from django.contrib import admin

class EditionAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'country', 'order', 'short_description',)
    ordering = ['order']

class EditionCategoryInline(admin.TabularInline):
    model = EditionCategory
    prepopulated_fields = {"url_name": ("name",)}
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'editions', 'color', 'active_color')
    inlines = [
        EditionCategoryInline,
    ]

class EditionWebsiteInline(admin.TabularInline):
    model = EditionWebsite
    extra = 1

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'editions', 'country', 'url')
    list_filter = ['category', 'country',]
    search_fields = ['title']
    ordering = ['category']
    inlines = [
        EditionWebsiteInline,
    ]

admin.site.register(Edition, EditionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Website, WebsiteAdmin)
