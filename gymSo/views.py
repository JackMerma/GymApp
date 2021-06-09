from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):

    dest1 = Destination() 
    dest1.name="Yoga"
    return render(request, "index.html", {'dest1': dest1})
