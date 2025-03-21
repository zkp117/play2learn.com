from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')  # Ensure correct path

def about_us(request):
    return render(request, 'pages/about_us.html')  # Ensure correct path
