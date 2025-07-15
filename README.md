```markdown
# 🚗 Sistema de Gestão de Concessionária

Desenvolvido por: [Yuri Lima](https://github.com/yuuri8), [Samuel Henrique](https://github.com/SamuelHenrique007)

Este sistema web, desenvolvido com Django e Bootstrap, tem como objetivo informatizar a gestão de uma concessionária de veículos. Ele substitui controles manuais por um sistema digital completo, permitindo o gerenciamento eficiente de funcionários, clientes, veículos, vendas e test-drives.

---

## 📋 Pré-requisitos

Certifique-se de que o Python está instalado na sua máquina:

```bash
python --version
```

---

## 🧪 Criar e ativar o ambiente virtual (venv)

1. Clone o repositório e crie o ambiente virtual na raiz do projeto:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
python -m venv venv
```

2. Ative o ambiente virtual:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux/macOS:**

```bash
source venv/bin/activate
```

---

## ⚙️ Configurar o banco de dados

Crie as tabelas com os comandos abaixo:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Criar o superusuário

Antes de acessar o sistema, crie um usuário administrador:

```bash
python manage.py createsuperuser
```

Informe um nome de usuário, senha e e-mail (opcional).

---

## 🚀 Executar o servidor de desenvolvimento

Execute o servidor local:

```bash
python manage.py runserver
```

Acesse o sistema pelo navegador no endereço:

```
http://127.0.0.1:8000/
```
⚠️ Atenção: o login no sistema só poderá ser feito com o usuário e senha do superusuário que você criou anteriormente.


---

## 🧩 Funcionalidades principais

* Login e logout de usuários
* Dashboard com indicadores e gráfico de vendas por mês
* Cadastro e edição de funcionários com permissões (Administrador ou Vendedor)
* Gerenciamento de clientes (CPF, telefone e nome)
* Cadastro de veículos com controle de disponibilidade
* Registro de vendas com valor, cliente, veículo e funcionário
* Agendamento e controle de test-drives

---

## 🎥 Demonstração em vídeo

*(Adicione aqui o link do vídeo, se houver)*

