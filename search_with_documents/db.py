from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from search_with_documents.settings import settings

engine = create_engine(url=settings.SQLITE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_session():
    session = Session()

    try:
        yield session

    finally:
        session.close()
