from django.shortcuts import render

from .models import (
    CommunityActivity,
    Testimonial
)

from services.models import Service


def home(request):

    activities = CommunityActivity.objects.all().order_by('-created_at')[:6]

    testimonials = Testimonial.objects.all()

    services = Service.objects.all()

    return render(
        request,
        'core/index.html',
        {
            'activities': activities,
            'testimonials': testimonials,
            'services': services,
        }
    )


def about(request):

    return render(request, 'core/about.html')


def solutions(request):

    return render(request, 'core/solutions.html')