from django.urls import include, path
from .views import homeView,sobreView,contatoView

urlpatterns = [
    path('',homeView,name='home'),
    path('sobre-nos/',sobreView,name='sobre-nos'),
    path('contato/',contatoView,name='contato'),
    #path('cadastro/',cadastroview.as_view(),name='cadastro'),
    
]