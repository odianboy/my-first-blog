from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_date', 'published_date')
    list_filter = ('author', 'title', 'text', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'


admin.site.register(Post, PostAdmin)
