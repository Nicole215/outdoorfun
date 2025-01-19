from . import views
from django.urls import path
from .views import OrganisatorDetailView


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('organisator/<int:pk>/', OrganisatorDetailView.as_view(), name='organisator_detail'),
]