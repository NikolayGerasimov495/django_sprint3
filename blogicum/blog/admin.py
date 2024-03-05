from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category'
    )


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
