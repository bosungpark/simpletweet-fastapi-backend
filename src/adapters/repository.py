from sqlalchemy.orm import Session

from src.adapters.orm import sqlalchemy_session
from src.domain.models import Tweet


class SqlAlchemyRepository:
    def __init__(self, session, model):
        self._session :Session = session
        self._model = model

    def add(self, product):
        self._session.add(product)

    def commit(self):
        self._session.commit()

    def list(self, column, value):
        col = getattr(self._model, column)
        return self._session.query(self._model).filter(col == value).all()

    def rollback(self):
        self._session.rollback()


tweet_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=sqlalchemy_session, model=Tweet)
