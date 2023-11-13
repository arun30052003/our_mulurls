from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def jadeja(request):
    return HttpResponse('<center><h1>->JADEJA<-</h1></center>'
        '<center><h3>All Rounder Of IPL...</h3></center>')