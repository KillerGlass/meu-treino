from django.shortcuts import render
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView,CreateView,ListView,DeleteView,DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import AlimentoRefeicaoDietaForm, ReceitasForm,PlanoDietaForm, RefeicaoDietaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



class CreateReceitasView(LoginRequiredMixin,CreateView):
    template_name = "dieta_form.html"
    model = Receitas
    form_class = ReceitasForm

    def get_success_url(self):
        messages.info(self.request,'Receita criada!!')
        
        return reverse_lazy('receitas-user')

    def form_valid(self, form):
        
        exercicio = form.save(commit=False) # salva os dados do form no bancos
        
        exercicio.categoria = form.cleaned_data['categoria']
        exercicio.user = self.request.user
        exercicio = form.save()  # salva os dados do form no banco


        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Criar Receita'
        context['botao'] = 'Criar'
        context['pagina'] = 'Receitas'

        return context

class ListReceitasView(ListView):
    model = Receitas
    template_name = "refeicoes.html"
    paginate_by = 6

class UpdateReceitasView(LoginRequiredMixin,UpdateView):

    model= Receitas
    template_name = "dieta_form.html"
    form_class = ReceitasForm

    def get_object(self):
        return get_object_or_404(Receitas,user=self.request.user,pk=self.kwargs['pk'])


    def get_success_url(self):
        messages.info(self.request,'Receita Atualizada!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Receita'
        context['botao'] = 'Salvar alterações'
        context['pagina'] = 'Receitas'

        return context

class DeleteReceitasView(DeleteView):
    template_name = "exercicios_form.html"
    model =  model= Receitas
    
    def get_success_url(self):
        messages.info(self.request,'Receitas Excluida!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_object(self):
        return get_object_or_404(Receitas,user=self.request.user,pk=self.kwargs['pk'])
      
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir a Receitas?'
        context['botao'] = 'Confirmar'
        context['pagina'] = 'Receitas'

        return context


class DetailReceitasView(DetailView):
    template_name = 'refeicao_detail.html'
    model = Receitas

class ListReceitasUserView(ListView):
    model = Receitas
    template_name = "refeicoes.html"
    paginate_by = 6

    def get_queryset(self):
        return self.request.user.receitas.all()

@login_required
def PlanoDietaView(request):
    template_name = "dieta.html"

    try:
        dieta = Plano_dieta.objects.get(user = request.user)
    except:
        dieta = None

    context = {}

    context['dieta'] = dieta

    return render(request,template_name,context)


@login_required
def CreatePlanoDietaView(request):
    template_name = "dieta_form.html"

    if request.method == 'POST': 
        form = PlanoDietaForm(request.POST, request.FILES)

        if form.is_valid(): 
            dieta = form.save(commit=False)
            dieta.user = request.user
            dieta = form.save()  # salva os dados do form no banco

            messages.info(request,'Plano de dieta criado!!')
            
            return redirect('dieta-manage',pk=dieta.pk)
    
    else:
        form = PlanoDietaForm()


    context = {}

    context['titulo'] = 'Criar Plano de Dieta'
    context['botao'] = 'Criar'
    context['pagina'] = 'Plano de Dieta'
    context['form'] = form

    return render(request,template_name,context)

@login_required 
def DeletePlanoDietaView(request,pk):
    template_name = "refeicoes_form.html"
    

    dieta = get_object_or_404(Plano_dieta,pk=pk,user=request.user)
    
    if request.method == 'POST': 
    
        messages.info(request,'Plano de Dieta Excluida!!')
        dieta.delete()

        return redirect('plano-dieta')

    context = {}
    context['titulo'] = 'Deseja Excluir o Plano de Dieta?'
    context['botao'] = 'Confirmar'

    return render(request,template_name,context)



@login_required
def Manage_plano_dieta(request,pk):
    template_name = "dieta_manage.html"

    dieta = get_object_or_404(Plano_dieta,pk=pk,user=request.user)
    
    context = {
        'dieta': dieta,
        'refeicoes': dieta.get_refeicoes()
        
    }

    return render(request,template_name,context)



@login_required
def CreateRefeicaoDietaView(request,pk):
    template_name = "refeicoes_form.html"

    if request.method == 'POST': 
        form = RefeicaoDietaForm(request.POST, request.FILES)

        if form.is_valid(): 
            refeicao = form.save(commit=False)
            refeicao.dieta = Plano_dieta.objects.get(pk=pk)
            refeicao = form.save()  # salva os dados do form no banco


            messages.info(request,'Refeição criada!!')

            return redirect('dieta-manage',pk=pk)
    
    else:
        form = RefeicaoDietaForm()

    context = {}

    context['titulo'] = 'Criar Refeição'
    context['botao'] = 'Criar'
    context['pagina'] = 'Plano de Dieta'
    context['form'] = form

    return render(request,template_name,context)


@login_required 
def DeleteRefeicaoView(request,pk_dieta,pk_refeicao):
    template_name = "refeicoes_form.html"
    

    dieta = get_object_or_404(Plano_dieta,pk=pk_dieta,user=request.user)
    refeicao = Refeicoes.objects.get(pk=pk_refeicao)
    
    if request.method == 'POST': 
    
        messages.info(request,'Refeicão Excluida!!')
        refeicao.delete()

        return redirect('dieta-manage',pk = pk_dieta)

    context = {}
    context['titulo'] = 'Deseja Excluir Refeicão?'
    context['botao'] = 'Confirmar'

    return render(request,template_name,context)


class UpdateRefeicaoView(LoginRequiredMixin,UpdateView):

    model= Refeicoes
    template_name = "refeicoes_form.html"
    fields = ['nome','tipo_refeicao']

    def get_object(self):

        dieta = get_object_or_404(Plano_dieta,pk=self.kwargs['pk_dieta'],user=self.request.user)
        
        return Refeicoes.objects.get(pk=self.kwargs['pk_refeicao'])


    def get_success_url(self):
        messages.info(self.request,'Refeição Atualizada!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Refeição'
        context['botao'] = 'Salvar alterações'


        return context



@login_required
def Manage_refeicao_dieta(request,pk_dieta,pk_refeicao):
    template_name = "refeicoes_manage.html"

    dieta = get_object_or_404(Plano_dieta,pk=pk_dieta,user=request.user)
    refeicao = get_object_or_404(Refeicoes,pk=pk_refeicao)
    
    context = {
        'dieta': dieta,
        'refeicao': refeicao,
        'alimentos': refeicao.get_alimentos()
        
    }

    return render(request,template_name,context)


@login_required
def CreateAlimentoRefeicaoView(request,pk_dieta,pk_refeicao):
    template_name = "refeicoes_form.html"

    dieta = get_object_or_404(Plano_dieta,pk=pk_dieta,user=request.user)
    refeicao = Refeicoes.objects.get(pk=pk_refeicao)
    print(refeicao)
    
    if request.method == 'POST': 
        form = AlimentoRefeicaoDietaForm(request.POST, request.FILES)

        if form.is_valid(): 
            alimento = form.save(commit=False)
            alimento.refeicao = refeicao
            alimento = form.save()  # salva os dados do form no banco

            messages.info(request,'Alimento adicionado a Refeição!!')

            return redirect('dieta-refeicao-manage',pk_dieta = pk_dieta,pk_refeicao = pk_refeicao)
    
    else:
        form = AlimentoRefeicaoDietaForm()

    context = {}

    context['titulo'] = 'Adcionar Alimento a Refeição'
    context['botao'] = 'Salvar'
    context['pagina'] = 'Plano de Dieta'
    context['form'] = form

    return render(request,template_name,context)

@login_required 
def DeleteAlimentoRefeicaoView(request,pk_dieta,pk_refeicao,pk_alimento):
    template_name = "refeicoes_form.html"
    

    dieta = get_object_or_404(Plano_dieta,pk=pk_dieta,user=request.user)
    refeicao = Refeicoes.objects.get(pk=pk_refeicao)
    alimento = Alimentos_da_Refeicao.objects.get(pk=pk_alimento)
    
    if request.method == 'POST': 
    
        messages.info(request,'Alimento da Refeicao Excluido!!')
        alimento.delete()

        return redirect('dieta-refeicao-manage',pk_dieta = pk_dieta,pk_refeicao = pk_refeicao)

    context = {}
    context['titulo'] = 'Deseja Excluir o Alimento da Refeicão?'
    context['botao'] = 'Confirmar'

    return render(request,template_name,context)


class UpdateAlimentoRefeicaoView(LoginRequiredMixin,UpdateView):

    model= Alimentos_da_Refeicao
    template_name = "refeicoes_form.html"
    fields = ['receita','quantidade']

    def get_object(self):

        dieta = get_object_or_404(Plano_dieta,pk=self.kwargs['pk_dieta'],user=self.request.user)
        refeicao = Refeicoes.objects.get(pk=self.kwargs['pk_refeicao'])

        return Alimentos_da_Refeicao.objects.get(pk=self.kwargs['pk_alimento'])


    def get_success_url(self):
        messages.info(self.request,'Alimento Atualizado!!')
        
        return self.request.GET.get('next',reverse_lazy('receitas'))

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Alimento'
        context['botao'] = 'Salvar alterações'


        return context

