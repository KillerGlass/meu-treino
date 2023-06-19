from django.urls import include, path
from .views import dietasView

urlpatterns = [
    path('dietas/',dietasView,name='dietas'),
    
]