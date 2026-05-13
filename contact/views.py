from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):

    form = ContactForm()

    success = False

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            success = True

            form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {
            'form': form,
            'success': success
        }
    )