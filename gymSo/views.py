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
    dest1.img='yoga-class.jpg'
    dest1.class_css='col-lg-4 col-md-6 col-12'

    dest2 = Destination() 
    dest2.name="Areobic"
    dest2.trainer="Mary"
    dest2.price=66
    dest2.desc=""
    dest2.img='crossfit-class.jpg'
    dest2.class_css='mt-5 mt-lg-0 mt-md-0 col-lg-4 col-md-6 col-12'

    dest3 = Destination() 
    dest3.name="Cardio"
    dest3.trainer="Cathe"
    dest3.price=75
    dest3.desc=""
    dest3.img='cardio-class.jpg'
    dest3.class_css='mt-5 mt-lg-0 col-lg-4 col-md-6 col-12'

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})
