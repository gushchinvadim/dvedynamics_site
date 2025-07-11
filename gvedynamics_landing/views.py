from django.shortcuts import render

from django.http import HttpResponse

def index_page(request):
    return render(request, 'gvedynamics_landing/index.html')
