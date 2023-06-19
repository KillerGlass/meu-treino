from django.shortcuts import render


def dietasView(request):      
    return render(request,template_name='home.html')
