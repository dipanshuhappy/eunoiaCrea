from django.shortcuts import render
from django.http import HttpResponse
def leadboard(request):
   
    return render(request,"leadboard.html")