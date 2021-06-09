from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):

    dest1 = Destination() 
    dest1.name="Yoga"
    dest1.trainer="Bella"
    dest1.price="55"
    return render(request, "index.html", {'dest1': dest1})
