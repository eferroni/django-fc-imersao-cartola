from django.urls import path
from .views import show_players


urlpatterns = [
    path('show_players', show_players)
]