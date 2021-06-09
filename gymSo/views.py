from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):

    dest1 = Destination() 
    dest1.name="Yoga"
    dest1.trainer="Bella"
    dest1.price=55
    dest1.desc=""

    dest2 = Destination() 
    dest2.name="Areobic"
    dest2.trainer="Mary"
    dest2.price=66
    dest2.desc=""

    dest3 = Destination() 
    dest3.name="Cardio"
    dest3.trainer="Cathe"
    dest3.price=75
    dest3.desc=""
    return render(request, "index.html", {'dest1': dest1, 'dest2':dest2, 'dest3':dest3})
