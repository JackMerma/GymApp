from django.shortcuts import render, redirect
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Ya existe este usuario")
            elif User.objects.filter(email=email).exists():
                print("Ya existe el email")
            else:
                user = User.objects.create(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('usuario creado')
        else:
            print("La contraseña no coincide...")

        return redirect('/')
    else:
        return render(request, 'register.html', {}) 
