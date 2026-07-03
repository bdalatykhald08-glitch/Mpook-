from django.shortcuts import render




# Create your views here.
def base(request):
  
    return render(request, 'base.html')

def masar(request):
    return render(request, 'pages/masar.html')

def blog(request):
    return render(request, 'pages/blog.html')

def major(request):
   
    return render(request, 'pages/major.html')
