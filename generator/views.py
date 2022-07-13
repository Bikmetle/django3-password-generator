from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ''
    char = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        char.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        char.extend(list('1234567890'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))

    for i in range(length):
        password += random.choice(char)

    return render(request, 'generator/password.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')
