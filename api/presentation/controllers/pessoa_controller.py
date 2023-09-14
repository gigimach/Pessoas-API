from fastapi import APIRouter, HTTPException, status, Header
from sqlmodel import Session, delete, select

from application.pessoa_service import PessoaService
from persistence.utils import obter_engine
from presentation.viewmodels.models import Pessoa


engine = obter_engine

router = APIRouter()
prefix = '/pessoa'

pesssoa_service = PessoaService()


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_pessoa(pessoa: Pessoa):

    if not pessoa:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Requisição Inválida')

    return pesssoa_service.criar_pessoa(pessoa)
     

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def obter_pessoa(id: int):
    pessoa = pesssoa_service.obter_pessoa_por_id(id)

    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pessoa não encontrada')
    
    return pessoa


@router.get('?t={termo_busca}', status_code=status.HTTP_200_OK)
async def busca_por_termo(termo: str):
    pessoas = pesssoa_service.busca_por_termo(termo)

    return pessoas


@router.get('/contagem-pessoas', status_code=status)
async def total_pessoas():
    return pesssoa_service.contagem_pessoas()