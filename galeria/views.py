from django.shortcuts import render

def menu(request):
    
    return render(request, 'menu.html')

def shopee(request):
    return render(request, 'shopee.html')

def amazon(request):
    return render(request, 'amazon.html')

def entrada(request):
    return render(request, 'entrada.html')

def saida(request):
    return render(request, 'saida.html')

def estoque(request):
    return render(request, 'estoque.html')

