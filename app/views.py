from django.shortcuts import render
from .models import Player


# Create your views here.
def show_players(request):
    players = Player.objects.all()
    return render(request, 'app/players.html', {'players': players})