from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from persistence.utils import obter_engine
from presentation.controllers.pessoa_controller import \
    prefix as pessoas_prefix
from presentation.controllers.pessoa_controller import \
    router as pessoas_router


app = FastAPI()

# Ativar CORS
origins = ['http://localhost:5500',
           'http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = obter_engine()
SQLModel.metadata.create_all(engine)

# Registrar Roteadores
app.include_router(pessoas_router, prefix=pessoas_prefix)
