from django.urls import path
from .views import incentivo, cadastrar_doador, lista_doadores

urlpatterns = [
    path('', incentivo, name='incentivo'),
    path('cadastrar/', cadastrar_doador, name='cadastrar_doador'),
    path('doadores/', lista_doadores, name='lista_doadores'),
]



