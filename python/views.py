from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def dhoni(request):
    return render(request,'dhoni.html')

def virat(request):
    return render(request,'virat.html')

def sachin(request):
    return render(request,'sachin.html')

def sushanth(request):
    return render(request,'sushanth.html')
