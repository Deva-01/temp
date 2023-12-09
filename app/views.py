from django.shortcuts import render

def page(request):
    return render(request,'sample.html')

def pages(request):
    a = "hema"
    return render(request,'s.html', {a:a})