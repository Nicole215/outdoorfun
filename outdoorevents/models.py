from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Organisator(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_info = models.TextField(blank=True, null=True)  # Add general information
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Event(models.Model):
    HIKING = 'Hiking'
    MUD_RUN = 'Mud Run'
    OTHER = 'Other'

    EVENT_TYPE_CHOICES = [
        (HIKING, 'Hiking'),
        (MUD_RUN, 'Mud Run'),
        (OTHER, 'Other'),
    ]

    organisator = models.ForeignKey(Organisator, on_delete=models.CASCADE, related_name="events")
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=OTHER)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return f"{self.organisator} - {self.date} - {self.town}"

    def save(self, *args, **kwargs):
        # Automatically generate a unique slug
        if not self.slug:
            self.slug = slugify(f"{self.organisator}-{self.town}-{self.date}")
        super().save(*args, **kwargs)