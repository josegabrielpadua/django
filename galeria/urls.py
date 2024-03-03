from galeria.views import menu, shopee
from django.urls import path

urlpatterns = [
        path('', menu, name='menu'),
        path('shopee/', shopee, name='shopee')
]