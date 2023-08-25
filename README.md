# 🐋Projeto de Questionário com Docker

# Objetivo:

O projeto tem como objetivo, a introdução ao `docker` e para isso foi passado a missão de criar um questionário simples e assim retornar se a resposta da pergunta está certa ou errada, com a particularidade de usar `docker` no banco de dados.

## 🐍Django:

Nesse projeto usamos o freamework `Django`, como pode ver no `requirements.txt` , usamos para atender a sugestão do professor de fazer tal projeto em `python` e pela facilidade do freamework com docker.

### Para usar o django:

Basta a criação de uma `virtualenv`, basta o uso do comando:

```python
python -m venv /path/to/new/virtual/environment
```

Para ativar a virtualenv:

```python
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

Com a `virtualenv`ativada basta baixar o `requirements.txt`, assim dando inicio ao `Django`. 
Para visualizar o projeto funcionando basta entrar na pasta do projeto:

```python
cd .\project_quiz\
```

E em seguida executar o projeto:

```python
python .\manage.py runserver
```

## 🐋Docker

Para o uso do docker basta estar com o `docker desctop` aberto e em seguida executar os seguintes comandos no terminal, que iram executar o arquivo `docker-compose`:
Para criar a build:

```python
ddocker-compose build
```

Para iniciar o serviço:

```python
docker-compose up
```

Assim todo o banco de dados irá para um “docker”.

## ⚙️Projeto

É um quiz simples onde a pergunta é comparada com a resposta e se clicar na correta sobe um `alert` para informar se é ou não a resposta correta.
Para criar uma nova pergunta basta acessar o `/admin` do projeto local `[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)` e para acessar basta criar um `superuser` para você, com o comando:

```python
python manage.py createsuperuser
```

Assim você terá acesso a parte administrativa do projeto onde poderá criar novas perguntas. 
#


https://github.com/Pedro-Prado-Dev/projeto_Questionario/assets/100048797/78f935a1-53b6-44d3-91cf-d6eabf002dbb

---

# 🐋Docker-based Questionnaire Project

# **Objective:**

The project aims to introduce Docker, and for this purpose, the task was assigned to create a simple questionnaire. It involves validating whether the answer to a question is correct or incorrect. The unique aspect of this project is the utilization of Docker for the database.

## **🐍Django:**

In this project, we use the **`Django`** framework. As you can see in the **`requirements.txt`** file, we opted for **`Python`** and the Django framework based on the professor's suggestion, owing to its ease of use with Docker.

### **Using Django:**

To utilize Django, simply create a **`virtualenv`** by running the command:

```python
pythonCopy code
python -m venv /path/to/new/virtual/environment

```

To activate the virtualenv:

```python

# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

With the virtualenv activated, download the **`requirements.txt`** file to kickstart Django. To view the project in action, navigate to the project folder:

```python

cd .\project_quiz\
```

Then execute the project:

```python

python .\manage.py runserver
```

## **🐋Docker:**

For Docker usage, ensure that **`Docker Desktop`** is open and then execute the following commands in the terminal. These commands will run the **`docker-compose`** file. 
To build:

```python

docker-compose build
```

To initiate the service:

```python

docker-compose up
```

This will containerize the entire database within a Docker environment.
## **⚙️Project**

This is a simple quiz application where a question is compared with an answer, and if the correct answer is clicked, an **`alert`** pops up to indicate its correctness. To add a new question, access the **`/admin`** section of the local project at **`http://127.0.0.1:8000/admin`**. To gain access, create a **`superuser`** account for yourself using the following command:

```python

python manage.py createsuperuser
```

This will grant you access to the project's administrative area, where you can create new questions.
#

https://github.com/Pedro-Prado-Dev/projeto_Questionario/assets/100048797/78f935a1-53b6-44d3-91cf-d6eabf002dbb
