from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def careers(request):

    return render(request, 'careers/careers.html')
