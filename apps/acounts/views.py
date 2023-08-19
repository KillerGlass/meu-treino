from datetime import datetime
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm  #form padrao para alteração de senha
from django.contrib.auth import authenticate,login #metodos de login
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.auxiliares.funcoes_auxiliares import compara_tempo

from .forms import Redefinir_senhaForm, UserCreationForm,UserChangeForm, UserUpdateForm

from .models import User,redefinir_senha
from django.contrib import messages

# Create your views here.
def cadastroview(request):
    if not request.user.is_authenticated: 
        template_name = "cadastro.html"

        if request.method == 'POST': 
            form = UserCreationForm(request.POST, request.FILES)

            if form.is_valid(): 
                user = form.save() 
                
                user = authenticate(username = user.username,password = form.cleaned_data['password1'])
                
                login(request,user)
                
                
                return redirect('cadastro-user2',pk=request.user.id)
        
        else:
            form = UserCreationForm()


        context = {}

        context['titulo'] = 'Registre-se'
        context['texto'] = 'Registre-se para acessar os recursos de nossa plataforma.'
        context['botao'] = 'Proximo'
        context['form'] = form

        return render(request,template_name,context)

class DateInput(forms.DateInput):
    input_type = 'date'
    
class cadastroview2(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'cadastro.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('home')

    def get_object(self):
        user = User.objects.get(pk=self.request.user.id)

        if user.ativo:
            erro = get_object_or_404(User,id=90123072387289)

        return user
    
    def form_valid(self, form):
        
        user = form.save(commit=False) # salva os dados do form no bancos
        
        user.ativo = True
        user = form.save()  # salva os dados do form no banco


        return super().form_valid(form)
    
    
    def get_form(self, form_class=None):
        form = super(cadastroview2, self).get_form(form_class)
        form.fields['nascimento'].widget = DateInput()
        return form
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        
        context['titulo'] = 'Informações Complementares'
        context['texto'] = 'Informe seus dados para concluir os cadastro na nossa plataforma.'
        context['botao'] = 'Finalizar cadastro'

        return context
    
class perfilView(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'perfil.html'
    form_class = UserUpdateForm

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get_success_url(self):
        messages.info(self.request,'Perfil Atualizado!!')
        
        return self.request.GET.get('next',reverse_lazy('perfil'))


class UpdatePasswordView(LoginRequiredMixin,UpdateView):

    model= User
    template_name = 'cadastro.html'
    
    def get_form(self, form_class= None):
        form = PasswordChangeForm(data= self.request.POST, user=self.request.user)
        return form    
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        
        context['titulo'] = 'Redefinição de senha'
        context['texto'] = 'Informe uma nova senha.'
        context['botao'] = 'Salvar'

        return context
    
    def get_success_url(self):
        messages.info(self.request,'Senha Atualizada, faça login para acessar sua conta!!')
        
        return self.request.GET.get('next',reverse_lazy('logout'))


def redefinir_senhaview(request):

    template_name = 'redefinir_senha.html'
    success = False
    success_msg = ''
    context = {}

    
    """form recebe o request.POST com os dados preenchidos do formulario se o form
       foi preenchido ou recebe None se o form ainda não foi preenchido
    """

    form = Redefinir_senhaForm(request.POST or None)  

    if form.is_valid():

        user = User.objects.get(email = form.cleaned_data['email'])

        #verifica se o usuario já possui algum pedido de redefinição de senha em aberto
        if redefinir_senha.objects.filter(User = user,confirmado = False).exists():
            success_msg = """Você já possui um pedido de redefinição de senha em aberto!
            Acesse seu E-mail e veja o E-mail que enviamos para voce com mais detalhes para 
            redefinir sua senha"""
        
        else:
            
            form.save()
            success_msg = 'E-mail confirmado com sucesso!! Foi enviado um E-mail para você com mais detalhes para redefinir sua senha'

        #indica se a operação ocorreu com sucesso
        success = True

    context['success'] = success
    context['form'] = form
    context['titulo'] = 'Redefinir senha'
    context['texto'] = 'Digite seu E-mail para redefinir senha'
    context['botao'] = 'Submeter'
    context['success_msg'] = success_msg
    
    return render(request,template_name,context)


"""
reset_passwordview é responsavel por redefinir a senha do usuario
recebe a chave que foi gerada pela solicitação de senha do usuario
e redefine a senha do user utilizando o form SetPasswordForm que
é um form padrao do django para redefinição de senha

"""
def reset_passwordview(request,key):

    template_name = 'redefinir_senha.html'
    context = {}

    success_msg = ''
    success = False

    #busca a solicitação do usuario no model redefinir senha
    reset = get_object_or_404(redefinir_senha,key=key)
    horario_atual = datetime.now().time()

    expirou = compara_tempo(horario_atual,reset.expira_em)

    if reset.confirmado or  expirou:
        form = SetPasswordForm(user = reset.User)
        
        success_msg = "OPs esté link já expirou! \n Não é mais possivel realizar esta operação!!"
        
        reset.confirmado = True
        reset.save()
        
        success = True

    else:
        form = SetPasswordForm(user = reset.User,data = request.POST or None)

        if form.is_valid():

            reset.confirmado = True
            reset.save()

            form.save()

            messages.info(request,"Sua senha foi redefinida com sucesso!!")

            return redirect(reverse_lazy('login'))
        
    context['success'] = success
    context['form'] = form
    context['titulo'] = 'Redefinir senha'
    context['botao'] = 'Confirmar'
    context['success_msg'] = success_msg

    return render(request,template_name,context)