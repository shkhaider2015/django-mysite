from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("t runs")
    return render(request, 'home.html')