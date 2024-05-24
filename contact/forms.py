from django import forms
from .models import ContactRequest
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.ModelForm):
    """
    A form for creating contact requests.

    Uses :model:`contact.ContactRequest`.

    **Fields and Labels**

        name: Name of the user.
        phone: Phone number of the user.
        email: Email address of the user.
        topic: Topic of interest for contacting the business.
        timeframe: Availability for a course if the user's interest is a course.
                   (Label: "Availability for a course")
        message: Additional message or comments from the user.

    **Methods**

    clean(self):
        Custom validation to ensure the phone number contains
        only digits, spaces, parentheses, + or -.
    """

    class Meta:
        model = ContactRequest
        fields = ("name", "phone", "email", "topic", "timeframe", "message")
        labels = {
            "name": "Name",
            "phone": "Phone",
            "email": "Email",
            "topic": "Topic",
            "timeframe": "Availability for a course",
            "message": "Message",
        }

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")

        if phone:
            """
            Regular expression to check if the phone field contains only
            digits, spaces, parentheses, + or -.
            """
            if not re.match(r"^[\d\s()+-]+$", phone):
                raise ValidationError(
                    "Phone number should contain only"
                    + " digits, spaces, parentheses, + or -."
                )
