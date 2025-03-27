from django.contrib import admin
from .models import Destination,News

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image_url')
    list_display_links = ('title','description','image_url')
    @admin.register(News)
    class NewsAdmin(admin.ModelAdmin):
        list_display = ('title', 'description','image_url','created_at'
)
