from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Participant
def leadboard(request):
   
    return render(request,"leadboard.html")


def leaderboard_data(request):
    results = Participant.objects.order_by("-scores")
    final = list(results.values())
    return JsonResponse(final,safe=False)