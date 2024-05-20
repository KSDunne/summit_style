from django import forms
from .models import ContactRequest
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.ModelForm):
    """
    A form for creating contact requests
    """

    class Meta:
        """
        Uses :model:`contact.ContactRequest`. This form
        collects information from users who want to contact the business.
        It includes fields for the user's name, phone, email, their topic of
        interest. If they chose course as an interest they can add
        the timeframe for when they are available to do the course.
        """

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
            if not re.match(r'^[\d\s()+-]+$', phone):
                raise ValidationError(
                    "Phone number should contain only"
                    + " digits, spaces, parentheses, + or -."
                )
