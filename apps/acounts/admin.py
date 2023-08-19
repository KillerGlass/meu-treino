from django.contrib import admin
from .models import User,redefinir_senha
# Register your models here.

admin.site.register(User)
admin.site.register(redefinir_senha)