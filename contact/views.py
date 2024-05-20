from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Views

"""
Credit: https://github.com/Code-Institute-Solutions/blog/blob/main/13_
collaboration_form/02_handle_the_POST_request/about/views.py#L6
"""


def contact_page(request):
    """
    Allows user contact requests.

    **Context**

    ``contact_form``
            An instance of :form:`contact.ContactForm`.

    **Template**

    :template:`contact/contact.html`
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Contact request received! We try to respond within"
                + " 2 working days.",
            )
        else:
            error_message = ("There was an error processing your request."
                             + " See error displayed on form.")
            messages.error(request, error_message)
            return render(
                request,
                "contact/contact.html",
                {"contact_form": contact_form, "error_message": error_message},
            )

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form},
    )
