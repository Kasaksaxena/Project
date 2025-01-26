from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def men(request):
    print("men page accessed")
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')