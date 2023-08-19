from django import forms

from apps.auxiliares.funcoes_auxiliares import trata_link, verifica_link
from .models import Receitas,Plano_dieta,Refeicoes,Alimentos_da_Refeicao

class ReceitasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['ingredientes'].widget.attrs.update({'class': 'form-control'})
        self.fields['preparo'].widget.attrs.update({'class': 'form-select'})
        self.fields['tempo_preparo'].widget.attrs.update({'class': 'form-control'})
        self.fields['calorias'].widget.attrs.update({'class': 'form-control'})
        self.fields['img'].widget.attrs.update({'class': 'form-select'})
        self.fields['video'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        

    categoria = forms.ChoiceField(
        choices=(('Almoço', 'Almoço'), 
                 ('Janta', 'Janta'),
                 ('Lanche', 'Lanche'),
                 ('Café da Manhã', 'Café da Manhã'), 
                 ('Lanche da manhã', 'Lanche da manhã'),
                 (' Lanche da tarde', ' Lanche da tarde'),
                 ('Ceia','Ceia'),
                 ('Sucos/Vitaminas', 'Sucos/Vitaminas'),
                 ('Frutas', 'Frutas'),
                 ('Doces','Doces'),
                 ('Sobremesa', 'Sobremesa'),
                 ('Suplementação', 'Suplementação'),
                 ('Outro', 'Outro')
                 ,), label='Categoria',widget=forms.Select(attrs={'class':"form-select"}))
     
    class Meta:
        model = Receitas

        fields = ["nome","ingredientes","preparo","tempo_preparo","calorias","img","video","categoria"]
     
     #função para validação do campo video
    def clean_video(self):
        
        if self.cleaned_data['video']:
            if verifica_link(self.cleaned_data['video']):
                video = self.cleaned_data['video']
                video = trata_link(video)
                
                return video
            else:
                raise forms.ValidationError('Por favor, digite um link valido!!')
        return '' 



class PlanoDietaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
    

    class Meta:
        model = Plano_dieta

        fields = ["nome"]
    
class RefeicaoDietaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_refeicao'].widget.attrs.update({'class': 'form-control'})
        

    tipo_refeicao = forms.ChoiceField(
        choices=(('Almoço', 'Almoço'), 
                 ('Janta', 'Janta'),
                 ('Lanche', 'Lanche'),
                 ('Café da Manhã', 'Café da Manhã'), 
                 ('Lanche da manhã', 'Lanche da manhã'),
                 (' Lanche da tarde', ' Lanche da tarde'),
                 ('Ceia','Ceia'),
                 ('Outro', 'Outro')
                 ,), label='tipo de refeicao',widget=forms.Select(attrs={'class':"form-select"}))
    
    class Meta:
        model = Refeicoes
        fields = ["nome","tipo_refeicao"]


    
class AlimentoRefeicaoDietaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receita'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Alimentos_da_Refeicao
        fields = ['receita','quantidade']


    
