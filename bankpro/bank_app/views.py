from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def apply(request):
    return render(request,'application.html')
def control(request):
    return render(request,'ctrl.html')
def about(request):
    return render(request,'about.html')

def test(request):
    if request.GET.get('Physics'):
        return render(request, 'homepage/home.html')
    else:
        return render(request, 'homepage/test2.html')