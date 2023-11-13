from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def tendulkar(request):
    return HttpResponse('<center><h1>->ARJUN TENDULKAR<-</h1></center>'
                        '<center><h3>Ghost Son...')


