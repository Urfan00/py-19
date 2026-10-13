from django.contrib import admin
from .models import Story



@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'publish_date', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('publish_date',)
    search_fields = ('title', 'description')
    ordering = ('-publish_date',)

