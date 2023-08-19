from django.urls import include, path
from .views import *

urlpatterns = [
    path('dietas/refeicoes/',ListReceitasView.as_view(),name='receitas'),
    path('dietas/refeicoes/create/',CreateReceitasView.as_view(),name='refeicao-create'),
    path('dietas/refeicoes/user/',ListReceitasUserView.as_view(),name='receitas-user'),
    path('dietas/refeicoes/update/<int:pk>/',UpdateReceitasView.as_view(),name='refeicao-update'),
    path('dietas/refeicoes/delete/<int:pk>/',DeleteReceitasView.as_view(),name='refeicao-delete'),
    path('dietas/refeicoes/detail/<int:pk>/',DetailReceitasView.as_view(),name='receitas-detail'),

    path('dietas/plan/',PlanoDietaView,name='plano-dieta'),
    path('dietas/plan/manage/<int:pk>/',Manage_plano_dieta,name='dieta-manage'),
    path('dietas/plan/create/',CreatePlanoDietaView,name='dieta-create'),
    path('dietas/plan/delete/<int:pk>',DeletePlanoDietaView,name='dieta-delete'),

    path('dietas/plan/refeicao/create/<int:pk>/',CreateRefeicaoDietaView,name='dieta-refeicao-create'),
    path('dietas/plan/refeicao/delete/<int:pk_dieta>/<int:pk_refeicao>/',DeleteRefeicaoView,name='dieta-refeicao-delete'),
    path('dietas/plan/refeicao/update/<int:pk_dieta>/<int:pk_refeicao>/',UpdateRefeicaoView.as_view(),name='dieta-refeicao-update'),
        
    path('dietas/plan/refeicoes/manage/<int:pk_dieta>/<int:pk_refeicao>/',Manage_refeicao_dieta,name='dieta-refeicao-manage'),
    path('dietas/plan/refeicao/create/alimento/<int:pk_dieta>/<int:pk_refeicao>/',CreateAlimentoRefeicaoView,name='dieta-refeicao-alimento-create'),
    path('dietas/plan/refeicao/delete/alimento/<int:pk_dieta>/<int:pk_refeicao>/<int:pk_alimento>/',DeleteAlimentoRefeicaoView,name='dieta-refeicao-alimento-delete'),
    path('dietas/plan/refeicao/update/alimento/<int:pk_dieta>/<int:pk_refeicao>/<int:pk_alimento>/',UpdateAlimentoRefeicaoView.as_view(),name='dieta-refeicao-alimento-update'),
    
]