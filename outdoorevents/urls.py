from . import views
from django.urls import path
from .views import EventList, OrganisatorDetailView


urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('organisator/<int:pk>/', OrganisatorDetailView.as_view(), name='organisator_detail'),
]