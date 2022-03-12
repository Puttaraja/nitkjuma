from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'About.html')