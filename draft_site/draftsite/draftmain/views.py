from django.shortcuts import render, get_object_or_404
from .models import Player

def index(request):
    return render(request, 'draftmain/index.html')


def playerView(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    print("I loaded player " + str(player.player_name))
    return render(request, 'draftmain/player.html', {'player': player})