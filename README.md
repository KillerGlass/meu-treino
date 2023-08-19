# Plataforma_Meu_Treino
 - Meu treino é uma plataforma web, onde os usuários podem criar treinos e dietas personalizados de acordo com suas necessidades e objetivos.

 ![alt text](./static/img/meu-treino.png)

# Rodando o Projeto
### - Requisitos
- Ter o python instalado
- Ter o pacote virtualenv instalado

### 1ª passo criar ambiente virtual e ativar

    virtualenv venv
### 2ª passo Ativar ambiente virtual
    . venv/bin/activate

### 3ª passo instalar dependencias

    pip install -r requirements.txt

### 4ª passo Criar banco de dados e tabelas

    pyton3 manage.py makemigrations
    pyton3 manage.py migrate

### 5ª passo(opcional) Criar usuario admin

    pyton3 manage.py createsuperuser

### 6ª passo rodar a aplicação

    pyton3 manage.py runserver

### 7ª passo Se divirta acessando a aplicação
-No seu browser favorito acesse

    http://localhost:8000/




    

