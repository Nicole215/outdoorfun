from django.shortcuts import render
from django.contrib import messages
from .models import FAQ
from .forms import ContactForm


def faqs_view(request):

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Contact request \
                received! Thank you for your submission.")

    faqs = FAQ.objects.all().order_by('order')
    contact_form = ContactForm()

    return render(request, 'faqs/faqs.html',
                  {'faqs': faqs, 'contact_form': contact_form},)