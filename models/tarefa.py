from typing import Self
from models.database import Database
from sqlite3 import Cursor


class Tarefa:
    def __init__(self: Self, titulo_tarefa: str, data_conclusao: str = None) -> None:
        self.titulo_tarefa: str = titulo_tarefa
        self.data_conclusao: str = data_conclusao

#Tarefa(tituo_tarefa"No"")

    @classmethod
    def id(cls, id: int):
        return cls(id_tarefa = id)

    def salvar_tarefa(self: Self) -> None:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)

    @staticmethod
    def obter_tarefas() -> list[Self]:
        with Database('./data/tarefas.sqlite3') as db:  
            query = 'SELCT titulo_tarefa, data_conclusao FROM tarefas;'
            resultados = db.buscar_tudo(query)
            tarefas: list[Self] = [Tarefa(titulo, data)for titulo, data in resultados ]
            return tarefas
        
    def excluir_tarefa(self):
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self)