from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):

    return render(request, 'core/index.html')


def about(request):

    return render(request, 'core/about.html')

def solutions(request):

    return render(request, 'core/solutions.html')





