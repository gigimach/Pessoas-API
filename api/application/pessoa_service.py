from fastapi import HTTPException, status
from sqlmodel import Session, select
from psycopg2.errors import UniqueViolation

from persistence.utils import obter_engine
from presentation.viewmodels.models import Pessoa

class PessoaService():
    def __init__(self):
        self.session = Session(obter_engine())


    def obter_todas_pesssoas(self):
        instrucao = select(Pessoa)
        pessoas = self.session.exec(instrucao).fetchall()

        return pessoas

    
    def criar_pessoa(self, pessoa: Pessoa):
        self.session.add(pessoa)

        if UniqueViolation:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Apelido já existe")

        self.session.commit()
        self.session.refresh(pessoa)
        self.session.close()

        return Pessoa
    

    def obter_pessoa_por_id(self, id: int):
        instrucao = select(Pessoa).where(Pessoa.id == id)
        pessoa = self.session.exec(instrucao).first()
        self.session.close()

        return pessoa
    

    def busca_por_termo(self, termo_busca: str):
        instrucao = select(Pessoa).where(Pessoa.apelido.contains(termo_busca) | Pessoa.nome.contains(termo_busca) | Pessoa.stack.contains(termo_busca))
        pessoas = self.session.exec(instrucao).fetchall()
        self.session.close()

        return pessoas
    

    def contagem_pessoas(self):
        instrucao = select(Pessoa)
        total_pessoas = self.session.exec(instrucao).fetchall()
        self.session.close()

        return {"contagem": len(total_pessoas)}
