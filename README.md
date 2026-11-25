# Human In & PlanPaz — Heroku-Ready Python Site

Clone em **Python (Flask + Jinja2 + WhiteNoise + Gunicorn)** das páginas do aplicativo **PlanPaz** (`/`) e institucional da **Human In** (`/humanin`), com todos os arquivos estáticos (CSS e imagens) hospedados localmente e prontos para deploy na Vercel ou Heroku.

## Estrutura do projeto

```text
human-in-site/
├── app.py                  # Aplicação Flask, rotas e headers de segurança
├── data.py                 # Conteúdo estruturado das páginas em Python
├── wsgi.py                 # Entrypoint WSGI para o Gunicorn (Heroku)
├── Procfile                # Processo web Heroku
├── requirements.txt        # Dependências Python
├── .python-version         # Versão Python para o buildpack heroku/python
├── static/
│   ├── css/
│   │   ├── styles.css      # CSS compilado (Tailwind + tokens OKLCH + animações)
│   │   └── custom.css      # Ajustes de scroll suave e [hidden]
│   ├── js/
│   │   └── main.js         # Header dinâmico, menu mobile, scroll, reveal e mailto
│   └── images/             # Logotipos, favicon, og-image e telas do PlanPaz
├── templates/
│   ├── base.html
│   ├── planpaz.html        # Página PlanPaz (/)
│   ├── index.html          # Página Human In (/humanin)
│   ├── 404.html
│   └── partials/
│       └── icons.html      # Macro Jinja2 com ícones SVG Lucide
└── tests/
    └── test_app.py         # Testes automatizados (unittest)
```

## Desenvolvimento local (Windows / Linux / macOS)

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

No Linux / macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Acesse:
- `http://127.0.0.1:5000/` (PlanPaz)
- `http://127.0.0.1:5000/humanin` (Human In)
- `http://127.0.0.1:5000/health` (Healthcheck JSON)

> **Nota para Windows:** `gunicorn` depende do módulo `fcntl` (exclusivo de sistemas Unix/Linux) e é executado no Heroku pelo `Procfile`. No Windows, utilize `python app.py` localmente.

## Executar testes

```bash
python -m unittest discover -s tests -v
```

## Deploy no Heroku

1. Inicialize o repositório Git (caso ainda não exista) e faça o primeiro commit:

```bash
git init
git add .
git commit -m "Initial commit: Human In & PlanPaz Flask site"
```

2. Crie o app no Heroku (com o buildpack oficial `heroku/python`) e envie o código:

```bash
heroku create nome-do-seu-app
heroku buildpacks:set heroku/python
git push heroku main
```

3. Abra o site publicado:

```bash
heroku open
```

> **Dica:** O formulário de contato em `/#contato` abre o cliente de e-mail (`mailto:contato@humanin.com.br`) exatamente como no site original. Caso queira envio direto pelo servidor no futuro, basta adicionar uma rota `POST /contato` em `app.py` integrando um provedor SMTP/API (como Resend ou SendGrid) via variáveis de ambiente (`heroku config:set`).
