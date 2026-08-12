from django.urls import path
from .views import get_fake_occupancy

urlpatterns = [
    path('occupancy/', get_fake_occupancy, name='fake-occupancy'),
]
