from django import forms

from apps.auxiliares.funcoes_auxiliares import trata_link, verifica_link
from .models import Exercicios,Treinos,Exercicios_do_treino
from multiselectfield import MultiSelectField

class ExerciciosForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        choices=(('Perna', 'Perna'), 
                 ('Peito', 'Peito'),
                 ('Costas', 'Costas'),
                 ('Bisceps', 'Bisceps'), 
                 ('Trisceps', 'Trisceps'),
                 ('Ombro', 'Ombro'),
                 ('Panturrilha','Panturrilha'),
                 ('Antebraço', 'Antebraço'),
                 ('Quadriceps', 'Quadriceps'), 
                 ('Posterior coxa', 'Posterior coxa'),
                 ('Abdominal', 'Abdominal'),
                 ('ABS', 'ABS'),
                 ('Powerlifting', 'powerlifting'), 
                 ('Calistenia', 'calistenia'),
                 ('Outro', 'Outro')
                 ,), label='Categoria')
     
    class Meta:
        model = Exercicios

        fields = ["nome","num_series","num_repeticoes","descanco","img","video","descricao","categoria"]
     
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

class TreinosForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        choices=(('Perna', 'Perna'), 
                 ('Peito', 'Peito'),
                 ('Costas', 'Costas'),
                 ('Biceps', 'Biceps'), 
                 ('Triceps', 'Triceps'),
                 ('Ombro', 'Ombro'),
                 ('Panturrilha','Panturrilha'),
                 ('Antebraço', 'Antebraço'),
                 ('Quadriceps', 'Quadriceps'), 
                 ('Posterior coxa', 'Posterior coxa'),
                 ('Abdominal', 'Abdominal'),
                 ('ABS', 'ABS'),
                 ('Powerlifting', 'powerlifting'), 
                 ('Calistenia', 'calistenia'),
                 ('Outro', 'Outro')
                 ,), label='Categoria')
     
    class Meta:
        model = Treinos

        fields = ['nome','img','descricao','categoria']

class ExerciciosTreinoForm(forms.Form):
    exercicios = Exercicios.objects.all()
    choices = []
    for i in exercicios:
        choices.append((i.id,i))
    
    exercicio = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=choices,label="Exercicios")
    
    class Meta:
        fields = ['exercicio']

class TreinoForm(forms.Form):
    
    class Meta:
        fields =['nome','descricao','img']
