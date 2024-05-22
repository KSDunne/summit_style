from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """

    list_display = (
        "name",
        "message",
        "topic",
        "timeframe",
        "read",
        "created_on",
    )
