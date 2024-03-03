from galeria.views import menu, shopee, amazon, entrada, estoque, saida
from django.urls import path

urlpatterns = [
        path('', menu, name='menu'),
        path('shopee/', shopee, name='shopee'),
        path('amazon/', amazon, name='amazon'),
        path('entrada/', entrada, name='entrada'),
        path('estoque/', estoque, name='estoque'),
        path('saída/', saida, name='saida')
]