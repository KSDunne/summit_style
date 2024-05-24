from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for creating order instances.

    **Fields**
        full_name: Full name of the customer.
        email: Email address of the customer.
        phone_number: Phone number of the customer.
        street_address1: First line of the customer's address.
        street_address2: Second line of the customer's address.
        town_or_city: Town or city of the customer's address.
        postcode: Postal code of the customer's address.
        country: Country of the customer's address.
        county: County, state, or locality of the customer's address.
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
