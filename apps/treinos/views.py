from django.shortcuts import render


def exerciciosView(request):      
    return render(request,template_name='exercicios.html')

def treinosView(request):      
    return render(request,template_name='treinos.html')