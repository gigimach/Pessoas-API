from sqlmodel import create_engine


def obter_engine():
    db_url = ''
    engine = create_engine(db_url, echo=True)

    return engine
