from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def example_of_extend(request):
    return render(request, 'website/example_of_extend.html')
