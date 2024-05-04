from django import forms
from .models import ContactRequest


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