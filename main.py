from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NomeInput(BaseModel):
    nome: str

@app.post("/alterar_nome")
def alterar_nome(nome_input: NomeInput):
    return {"mensagem": f"{nome_input.nome}"}

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API FastAPI"}

@app.get("/usuario")
def usuario():
    return {"nome": "Maria", "idade": 25}

@app.get("/produto")
def produto():
    return {"produto": "Notebook", "preco": 3500}

@app.get("/mensagem")
def mensagem():
    return {"mensagem": "Olá mundo!"}


