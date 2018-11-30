from django.shortcuts import render

def home(request):
    return render(request, 'basic/home.html')