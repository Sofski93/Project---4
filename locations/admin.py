from django.contrib import admin
from .models import Location, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Location)
class LocationAdmin(SummernoteModelAdmin):
    """
    This class details the attributes available on the backend for the 
    Location posts
    """
    list_display = ('title', 'slug', 'status', 'created_at', 'creator')
    search_fields = ['content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_at')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class details the attributes available on the backend for the 
    Comments
    """
    list_display = ('name', 'body', 'location', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'body')