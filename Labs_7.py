from http.client import HTTPException

from dulwich.porcelain import status
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Gerenciador de Tarefas", version="1.0")
class Tarefa(BaseModel):
    nome: str
    descricao: str
tarefas = []
@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    for t in tarefas:
        if t["nome"].lower() == tarefa.nome.lower():
            raise HTTPException(status_code=400, detail="Já existe uma tarefa com esse nome")
    nova_tarefa = {
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso!", "tarefa": nova_tarefa}
@app.get("/tarefas")
def listar_tarefas():
    return{"tarefas": tarefas}
@app.put("/tarefas/{nome}")
def concluir_tarefa(nome: str):
    for t in tarefas:
        if t["nome"].lower() == nome.lower():
            t["concluida"] = True
            return {"mensagem": f"Tarefa {nome} marcada como concluida!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str):
    for t in tarefas:
        if t["nome"].lower() == nome.lower():
            tarefas.remove(t)
            return {"mensagem": f"Tarefa {nome} removida com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")