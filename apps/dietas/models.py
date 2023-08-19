from django.db import models
from apps.acounts.models import User

class Receitas(models.Model):
    nome = models.CharField('Nome',max_length=100)
    ingredientes = models.TextField("Ingredientes")
    preparo = models.TextField("Preparo")
    tempo_preparo = models.CharField("Tempo de Preparo",max_length=100)
    calorias = models.PositiveIntegerField("Calorias")
    img = models.ImageField(upload_to='dietas/imagens',verbose_name='imagem descritiva',null=True,blank=True)
    video = models.CharField('link do Video descritivo',max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='receitas')
    categoria = models.CharField("Categoria",max_length=100,blank=False)
    criado_em= models.DateTimeField('criado em: ',auto_now_add=True)
    atualizado_em= models.DateTimeField('atualizado em: ',auto_now=True)

    def __str__(self):
        return self.nome

class Plano_dieta(models.Model):
    nome = models.CharField('nome',max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT,related_name='dieta')
    criado_em= models.DateTimeField('criado em: ',auto_now_add=True)
    atualizado_em= models.DateTimeField('atualizado em: ',auto_now=True)

    def get_refeicoes(self):
        return self.refeicoes.all()

    def __str__(self):
        return self.nome
    
        
class Refeicoes(models.Model):
    nome = models.CharField('nome',max_length=100)
    tipo_refeicao = models.CharField("Tipo de Refeição", max_length=100,blank=True)
    total_calorias = models.IntegerField("Total de calorias",blank=True,null=True)
    dieta = models.ForeignKey(Plano_dieta,on_delete=models.CASCADE,related_name='refeicoes')

    def get_alimentos(self):
        return self.alimentos.all()
    
    def __str__(self):
        return f"Refeições do {self.dieta}"

class Alimentos_da_Refeicao(models.Model):
    quantidade  = models.CharField('Quantidade',max_length=200,null=True)
    refeicao = models.ForeignKey(Refeicoes,on_delete=models.CASCADE,related_name='alimentos')
    receita = models.ForeignKey(Receitas,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Alimentos da Refeição"

