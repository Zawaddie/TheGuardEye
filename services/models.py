from django.db import models

# Create your models here.


class Service(models.Model):

    title = models.CharField(max_length=200)

    icon = models.CharField(max_length=100)

    short_description = models.TextField()

    full_description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title
