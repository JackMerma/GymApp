from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso 

# Create your views here.
def home(request):

    dests = Curso.objects.all()

    return render(request, "index.html", {'dests': dests})
