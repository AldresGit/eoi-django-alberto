from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'text', 'created_date', 'published_date')
    list_filter = ('created_date', 'author')
    date_hierarchy = 'created_date'


admin.site.register(Post)