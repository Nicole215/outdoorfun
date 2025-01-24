from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Event, Organisator
from django.db.models import Q


class EventList(generic.ListView):
    model = Event
    template_name = "outdoorevents/index.html"
    context_object_name = "event_list"
    paginate_by = 6

    def get_queryset(self):
        queryset = Event.objects.all().order_by("date")  # Default to all events, ordered by date
        query = self.request.GET.get("q") # Get the search query from the URL
        if query:
            queryset = queryset.filter(
                Q(event_type__icontains=query) | 
                Q(town__icontains=query) | 
                Q(country__icontains=query) |
                Q(organisator__name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")  # Pass the query to the template
        return context


class OrganisatorDetailView(DetailView):
    model = Organisator
    template_name = 'outdoorevents/organisator_detail.html'
    context_object_name = 'organisator'