from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doadores/', include('doadores_artigos.urls')),
    path('', lambda request: redirect('doadores/')),  # Redireciona a URL raiz para 'doadores/'
]
