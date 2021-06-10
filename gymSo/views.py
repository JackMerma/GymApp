from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):

    cursos = Curso.objects.all()
    responsables = Responsable.objects.all() 

    return render(request, "index.html", {'cursos': cursos, 'responsables': responsables})

