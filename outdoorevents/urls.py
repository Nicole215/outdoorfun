from . import views
from django.urls import path
from .views import EventList, OrganisatorDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('organisator/<int:pk>/', OrganisatorDetailView.as_view(),
         name='organisator_detail'),
]
