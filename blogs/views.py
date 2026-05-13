from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def blogs(request):

    return render(request, 'blogs/blogs.html')


    
