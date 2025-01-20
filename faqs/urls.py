from django.urls import path
from . import views
from .views import faqs_view

urlpatterns = [
    path('', faqs_view, name='faqs'),
]