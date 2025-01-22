from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from .models import Event, Organisator


class EventList(generic.ListView):
    queryset = Event.objects.all().order_by('date')  # Order events by date
    template_name = "outdoorevents/index.html"
    paginate_by = 6


class OrganisatorDetailView(DetailView):
    model = Organisator
    template_name = 'outdoorevents/organisator_detail.html'
    context_object_name = 'organisator'