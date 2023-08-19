from django.db import models
from apps.acounts.models import User

class Exercicios(models.Model):
    nome = models.CharField('nome',max_length=100)
    num_series = models.PositiveIntegerField("numero de series")
    num_repeticoes = models.PositiveIntegerField("numero de repeticoes")
    descanco = models.CharField("Tempo de descanço",max_length=100)
    img = models.ImageField(upload_to='exercicios/imagens',verbose_name='imagem descritiva',null=True,blank=True)
    video = models.CharField('link do Video descritivo',max_length=100,blank=True)
    descricao = models.TextField("Descricao",blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='exercicios')
    categoria = models.CharField("Categoria",max_length=100,blank=False)
    criado_em= models.DateTimeField('criado em: ',auto_now_add=True)
    atualizado_em= models.DateTimeField('atualizado em: ',auto_now=True)


    def __str__(self):
        return self.nome


class Treinos(models.Model):
    nome = models.CharField('nome',max_length=100)
    descricao = models.TextField("Descricao",blank=True)
    img = models.ImageField(upload_to='treinos/imagens',verbose_name='imagem descritiva',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='treinos')
    categoria = models.CharField("Categoria",max_length=100,blank=False)
    criado_em= models.DateTimeField('criado em: ',auto_now_add=True)
    atualizado_em= models.DateTimeField('atualizado em: ',auto_now=True)

    def __str__(self):
        return self.nome
    
    def get_exercicios_treino(self):
        exercicios = []
        for i in self.exercicios_do_treino.all():
            exercicios.append(i.exercicio)
        
        return exercicios
        
class Exercicios_do_treino(models.Model):
    exercicio = models.ForeignKey(Exercicios,on_delete=models.CASCADE,related_name='exercicio_do_treino')
    treino = models.ForeignKey(Treinos,on_delete=models.CASCADE,related_name='exercicios_do_treino')

    def __str__(self):
        return f" Exercicios do {self.treino}"

