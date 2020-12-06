from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_date', 'published_date', 'cover')
    list_filter = ('author', 'title', 'text', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author', 'text')


admin.site.register(Comment, CommentAdmin)