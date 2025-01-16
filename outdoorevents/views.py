from django.shortcuts import render
from django.views import generic
from .models import Event, Organisator


class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "outdoorevents/index.html"
    paginate_by = 6