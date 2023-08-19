from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from Meu_Treino.settings import AUTH_USER_MODEL
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(AbstractUser):
    
    nome = models.CharField('Nome completo',max_length=100,null=True,blank=True)
    imageperfil = models.ImageField(upload_to='perfil/imagens',verbose_name='imagem perfil',null=True,blank=True)
    email = models.EmailField('E-mail',blank=False,unique=True)
    nascimento = models.DateField("Data de Nascimento",null=True,blank=True)
    sexo = models.CharField('Sexo',max_length=100,null=True,blank=True)
    peso = models.DecimalField("Peso",max_digits=4,decimal_places=2,null=True,blank=True, 
                               validators=[MinValueValidator(10),MaxValueValidator(200)])
    altura = models.DecimalField("Altura",max_digits=3,decimal_places=2,null=True,blank=True,
                                 validators=[MinValueValidator(1),MaxValueValidator(2)])
    
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return f"{self.username}"


class redefinir_senha(models.Model):

    User = models.ForeignKey(User,verbose_name='Usuario', related_name='resets',on_delete=models.PROTECT)
    key = models.TextField('key',max_length=100,unique=True)
    criado_em = models.DateField('Data criação',auto_now=True)
    confirmado = models.BooleanField('Senha foi redefinida:',default=False)
    horario = models.TimeField('horario de criação',auto_now=True)
    expira_em = models.TimeField('tempo para expirar',null=True)

    def __str__(self):
        return f"{self.User} {self.criado_em}"
    
    class meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-criado_em']


