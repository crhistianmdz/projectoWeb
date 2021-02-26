from django.urls import path
from ProjectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home,name='Home'),
    path('tienda/', views.tienda,name='Tienda'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#creacion de las rutas de imagenes cuando el servidor pasa a ser de desarrollo a produccion