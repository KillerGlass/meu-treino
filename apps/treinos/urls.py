from django.urls import include, path
from .views import treinosView,exerciciosView

urlpatterns = [
    path('treinos/',treinosView,name='treinos'),
    path('exercicios/',exerciciosView,name='exercicios'),
    
]