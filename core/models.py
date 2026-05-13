from django.db import models

# Create your models here.


class CommunityActivity(models.Model):

    ACTIVITY_TYPES = (

        ('mentorship', 'Mentorship'),

        ('conference', 'Conference'),

        ('team_building', 'Team Building'),

        ('workshop', 'Workshop'),

        ('community', 'Community Engagement'),

    )

    title = models.CharField(
        max_length=250
    )

    activity_type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPES
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='community/images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='community/videos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


class Testimonial(models.Model):

    client_name = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200
    )

    feedback = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.client_name

