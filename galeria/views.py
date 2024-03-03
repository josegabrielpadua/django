from django.shortcuts import render

def menu(request):
    
    return render(request, 'menu.html')

def shopee(request):
    return render(request, 'shopee.html')
