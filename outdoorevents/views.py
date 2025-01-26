from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Event, Organisator
from django.db.models import Q


class EventList(generic.ListView):
    """
    View to display paginated list of events.
    Includes search functionality to filter events by type, town, country,
    or organisator's name.
    """
    model = Event
    template_name = "outdoorevents/index.html"
    context_object_name = "event_list"
    paginate_by = 6

    def get_queryset(self):
        """
        Returns a filtered queryset of events.
        If a search query ('q') is provided in the URL parameters, filters
        events based on event type, town, country, or organisator's name.
        Otherwise, returns all events ordered by date.
        """
        queryset = Event.objects.all().order_by("date")  # Default queryset
        query = self.request.GET.get("q")  # Get the search query
        if query:
            queryset = queryset.filter(
                Q(event_type__icontains=query) |
                Q(town__icontains=query) |
                Q(country__icontains=query) |
                Q(organisator__name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds the search query ('q') to the context for use in the template.
        """
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class OrganisatorDetailView(DetailView):
    """
    View to display details of a specific organiser.
    """
    model = Organisator
    template_name = 'outdoorevents/organisator_detail.html'
    context_object_name = 'organisator'

    def get_context_data(self, **kwargs):
        """
        Add a sorted list of events related to the organisator to the context.
        """
        context = super().get_context_data(**kwargs)
        # Order events by date
        context['events'] = self.object.events.all().order_by('date')
        return context
