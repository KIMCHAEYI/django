from django.shortcuts import render

def home(request): 
    return render(request, 'index.html') #어떤 요청이 들어왔을 때, 요청과 함께 index.html을 보내라

def test(request): 
    return render(request, 'test.html')