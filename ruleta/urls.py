from django.urls import path 
from . import views

urlpatterns = [
    path('jugar/', views.jugar_ruleta, name='jugar_ruleta'),
    path('Ruleta', views.ruleta_page, name='Ruleta'),
    path('', views.ruleta_page2, name='inicio')
] 