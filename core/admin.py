from django.contrib import admin

from .models import (
    CommunityActivity,
    Testimonial
)

# Register your models here.

admin.site.register(CommunityActivity)

admin.site.register(Testimonial)


