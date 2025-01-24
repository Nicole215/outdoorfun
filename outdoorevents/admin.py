from django.contrib import admin
from django.utils.html import format_html
from .models import Organisator, Event


@admin.register(Organisator)
class OrganisatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'display_image')

    def display_image(self, obj):
        if obj.image:  # Check if the Organisator has an image
            return format_html(
                f'<img src="{obj.image.url}" style="max-height: 50px;">')
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('organisator', 'event_type', 'town', 'country',
                    'date', 'slug')
    list_filter = ('event_type', 'town', 'country', 'date')
    search_fields = ('organisator__name', 'town', 'country', 'event_type')
