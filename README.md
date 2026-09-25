# Nome do Projeto

Projeto full-stack com **Vue.js** no frontend, **Python (Django)** no backend e **PostgreSQL** como banco de dados.

## 🛠️ Tecnologias

- Python / Django
- Vue.js (Vite)
- PostgreSQL

## 📋 Pré-requisitos

- Python 3.x
- Node.js e npm
- PostgreSQL ativo
- Ambiente virtual Python configurado (`.venv`)

## 🚀 Executar o projeto

### Backend

Com o PostgreSQL ativo e o arquivo `saves.env` configurado:

```powershell
..\.venv\Scripts\Activate.ps1
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

Em outro terminal:

```powershell
cd frontend
npm install
npm run dev
```

O frontend acessa `http://127.0.0.1:8000/api/usuarios/` através do proxy do Vite.

## 📁 Estrutura do projeto
