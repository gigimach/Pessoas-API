from sqlmodel import create_engine


def obter_engine():
    db_url = 'postgresql+psycopg2://pessoasdb_user:E8WioqKwy99EusBayVA9mo43x00xGgEV@dpg-ck1p2qn03lhc73fdm0e0-a.oregon-postgres.render.com/pessoasdb'
    engine = create_engine(db_url, echo=True)

    return engine
