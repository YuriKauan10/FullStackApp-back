from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Liberar frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variáveis para armazenar dados
dados_armazenados = {}

# Modelo para os dados recebidos
class Dados(BaseModel):
    usuario: str
    produto: str
    mensagem: str

@app.post("/enviar")
def receber_dados(dados: Dados):
    dados_armazenados['usuario'] = dados.usuario
    dados_armazenados['produto'] = dados.produto
    dados_armazenados['mensagem'] = dados.mensagem
    return {
        "usuario": "Dados recebidos com sucesso!",
        "produto": "Dados recebidos com sucesso!",
        "mensagem": "Dados recebidos com sucesso!"
    }


# Função GET para acessar o usuário
@app.get("/usuario")
def obter_usuario():
    return {"usuario": dados_armazenados.get("usuario", "Não informado")}

# Função GET para acessar o produto
@app.get("/produto")
def obter_produto():
    return {"produto": dados_armazenados.get("produto", "Não informado")}

# Função GET para acessar a mensagem
@app.get("/mensagem")
def obter_mensagem():
    return {"mensagem": dados_armazenados.get("mensagem", "Não informada")}

