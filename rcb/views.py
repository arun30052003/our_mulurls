from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def kallis(request):
    return HttpResponse('<center><h1>->JACQUES KALLIS<-</h1></center'
        '<center><h3>African All Rounder...</h3><center>')