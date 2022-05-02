
# Projeto &ldquo;API da Geek University&rdquo;

## Introdução
O objetivo deste projeto é registrar os meus testes, insights e prática obtida com o curso [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/), ministrado pela [Geek University](https://geekuniversity.com.br/).

O código é escrito em Python, utilizando [Django REST Framework](https://www.django-rest-framework.org/).

Se trata de uma API RESTful, que manipula dados de cursos e avaliações.


# Requisitos
- Python 3.8 ou superior
- Pip
- Virtualenv

Após instalados e configurados os requisitos, siga a leitura.


# Rodando o projeto
Para rodar o servidor em modo de produção, você deverá:
1. Criar e/ou ativar um ambiente virtual, usando o virtualenv **(opcional)**
2. Instalar as dependências do projeto
3. Fazer as migrações 
4. Rodar o servidor em modo de produção

Instruções abaixo.

## 1. Ambiente virtual (opcional)
A criação do ambiente virtual é opcional, porém recomendado. Ela isola o ambiente real Python e impede que você faça modificações na instalação original, criando uma nova instalação Python. A diferença é que o Python da Virtualenv vem totalmente limpo.

Você pode ignorar estas etapas, por sua conta e risco.

### Criando o ambiente virtual
Para criar o ambiente virtual, abra o seu Terminal e digite

	$ python3 -m venv <nome-do-ambiente-virtual>

substitituindo <var>nome-do-ambiente-virtual</var> por um nome de sua escolha. Este será o nome dado ao ambiente virtual.

**OBS:** após executar o comando, o sistema criará uma pasta com o nome que você escolheu no local em que seu shell está sendo executado.

### Ativando o ambiente virtual
Para ativar o ambiente virtual criado, abra o Terminal na pasta onde o sistema criou a pasta do passo anterior, e digite

	$ source <nome-do-ambiente_virtual>/bin/activate

## 2. Instalando as dependências do projeto
Para que o servidor rode, é preciso instalar as dependências do projeto usando o pip. Para tanto, abra o Terminal, navegue até o diretório do projeto e digite

	$ pip install -r requirements.txt

## 3. Fazendo as migrações
Para que o banco de dados seja criado, é preciso fazer as migrações. Esse processo cria um banco de dados SQLite, usando as especificações dos models. No Terminal, dentro do diretório do projeto, digite

	$ python3 manage.py migrate

Após executado o comando, o sistema criará um arquivo de banco da dados chamado **db.sqiite3** na raíz do projeto.

## 4. Rodando o servidor em modo de produção

Com o Terminal aberto no diretório do projeto, digite
	
	$ python3 manage.py runserver
