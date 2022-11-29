from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "backend_test/index.html")

def map(request):
    return render(request, "backend_test/map.html")

def map2(request):
    return render(request, "backend_test/map2.html")