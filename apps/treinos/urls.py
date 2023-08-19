from django.urls import include, path
from .views import *

urlpatterns = [
    path('exercicios/',ListExerciciosView.as_view(),name='exercicios'),
    path('exercicios/user/',ListExerciciosUserView.as_view(),name='exercicios-user'),
    path('exercicios/create/',CreateExercicioView.as_view(),name='exercicios-create'),
    path('exercicios/update/<int:pk>/',UpdateExerciciosView.as_view(),name='exercicios-update'),
    path('exercicios/delete/<int:pk>/',DeleteExerciciosView.as_view(),name='exercicios-delete'),
    path('exercicios/detail/<int:pk>/',DetailExerciciosView.as_view(),name='exercicios-detail'),
    path('treinos/',ListTreinosView.as_view(),name='treinos'),
    path('treinos/user/',ListTreinosUserView.as_view(),name='treinos-user'),
    path('treinos/update/<int:pk>/',UpdateTreinoView.as_view(),name='treinos-update'), 
    path('treinos/delete/<int:pk>/',DeleteTreinosView.as_view(),name='treinos-delete'), 
    path('treinos/detail/<int:pk>/',DetailExerciciosTreinoView,name='treinos-detail'), 
    path('treinos/create/',CreateTreinoView,name='treinos-create'),
    path('treinos/manage/<int:pk>/',treinos_manage,name='treinos-manage'), 
    path('treinos/exercicios-treino/create/<int:pk>/',CreateExerciciosTreino,name='treinos-create-exercicios'),
    path('treinos/exercicios-treino/delete/<int:id_treino>/<int:id_ex>/',DeleteExerciciosTreinoView,name='treinos-exercicios-delete'),
    
    
    
]