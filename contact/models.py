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
    Stores a single contact message
    """

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField()
    topic = models.TextField(choices=TOPICS)
    timeframe = models.TextField(choices=TIMEFRAME)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Contact request from {self.name}"