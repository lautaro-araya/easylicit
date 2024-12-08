from django.urls import path
from core import views

    
urlpatterns = [
    path('',views.iniciar_sesion, name='iniciar_sesion'),
    path('home',views.home, name='home'),
    path('upload_excel',views.upload_excel, name='upload_excel'),
    path('convert_excel',views.convert_excel, name='convert_excel'),
]