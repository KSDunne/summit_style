from django.db import models

TOPICS = (
    ("Clothes Topic", "Clothes"),
    ("Equipment Topic", "Equipment"),
    ("Courses Topic", "Courses"),
    ("Other Topic", "Other"),
)

TIMEFRAME = (
    ("Days Timeframe", "Within days"),
    ("Weeks Timeframe", "Within weeks"),
    ("Months Timeframe", "Within a few months"),
    ("Year Timeframe", "In a year"),
    ("Unsure Timefram", "Unsure"),
)

# Models


class ContactRequest(models.Model):
    """
    Stores a single contact message.

    Fields:
        - `name` (CharField): Name of the sender.
        - `phone` (CharField): Phone number of the sender (optional).
        - `email` (EmailField): Email address of the sender.
        - `topic` (TextField): Topic of the message chosen from
            predefined choices.
        - `timeframe` (TextField): Timeframe specified by the
            sender (optional).
        - `message` (TextField): Content of the message.
        - `read` (BooleanField): Indicates whether the message has been read.
        - `created_on` (DateTimeField): Date and time when the message
            was created.

    Meta:
        - `ordering`: Ordering for queries based on creation date.

    Methods:
        - `__str__`: String representation of the contact request.
    """

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField()
    topic = models.TextField(choices=TOPICS)
    timeframe = models.TextField(choices=TIMEFRAME, null=True, blank=True)
    message = models.TextField(max_length=900)
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Contact request from {self.name}"
