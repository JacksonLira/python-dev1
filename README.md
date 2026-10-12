# Python Dev Profile

Minha primeira API desenvolvida com Python e FastAPI.

## Tecnologias

* Python
* FastAPI
* Uvicorn

## Funcionalidades

* Rota inicial da API
* Verificação de saúde da aplicação
* Consulta de perfil
* Consulta de habilidades técnicas

## Instalação

Clone o repositório e entre na pasta do projeto.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação da API:

http://127.0.0.1:8000/docs
