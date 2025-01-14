from django.contrib import admin
from .models import Organisator, Event


@admin.register(Organisator)
class OrganisatorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('organisator', 'event_type', 'town', 'country', 'date', 'slug')
    list_filter = ('event_type', 'town', 'country', 'date')
    search_fields = ('organisator__name', 'town', 'country', 'event_type')