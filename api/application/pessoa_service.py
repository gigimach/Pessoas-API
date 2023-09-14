from fastapi import HTTPException, status
from sqlalchemy import delete
from sqlmodel import Session, delete, select

from persistence.utils import obter_engine
from presentation.viewmodels.models import Pessoa

class PessoaService():
    def __init__(self):
        self.session = Session(obter_engine())
    

    def criar_pessoa(self, pessoa: Pessoa):
        self.session.add(pessoa)
        self.session.commit()
        self.refresh(pessoa)
        self.session.close()

        return Pessoa
    

    def obter_pessoa_por_id(self, id: int):
        instrucao = select(Pessoa).where(Pessoa.id == id)
        pessoa = self.session.exec(instrucao).first()
        self.session.close()

        return pessoa
    

    def busca_por_termo(self, termo: str):
        instrucao = select(Pessoa).where(termo in Pessoa)
        pessoas = self.session.exec(instrucao).fetchall()
        self.session.close()

        return pessoas
    

    def contagem_pessoas(self):
        instrucao = select(Pessoa)
        total_pessoas = self.session.exec(instrucao).fetchall()
        self.session.close()

        return len(total_pessoas)
