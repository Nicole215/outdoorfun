from django.contrib import admin
from .models import FAQ, ContactRequest


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'order',
    )
    search_fields = (
        'question',
        'answer',
    )
    ordering = ('order',)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
