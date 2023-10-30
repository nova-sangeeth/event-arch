"""
Backend : db
==============
This package contains the configuration for db 
"""
__author__ = "novasangeeth@outlook.com"


from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Initialize the declarative Base

Base = declarative_base()


# Define a custom class for the declarative base with a different name.
class ORMBase:
    def as_dict(self) -> dict:
        result: dict = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return

    @classmethod
    def create(cls, session, **kwargs):
        instance = cls(**kwargs)
        session.add(instance)
        session.commit()
        return instance

    @classmethod
    def update(cls, session, filter_by, **kwargs):
        session.query(cls).filter_by(**filter_by).update(kwargs)
        session.commit()

    @classmethod
    def delete(cls, session, filter_by):
        session.query(cls).filter_by(**filter_by).delete()
        session.commit()

    @classmethod
    def read(cls, session, filter_by=None, order_by=None):
        query = session.query(cls)
        if filter_by:
            query = query.filter_by(**filter_by)
        if order_by:
            query = query.order_by(order_by)
        return query.all()

    @classmethod
    def read_by_id(cls, session, row_id):
        return session.query(cls).filter_by(id=row_id).first()

    @classmethod
    def read_by_column(cls, session, column_name, value):
        filter_dict = {column_name: value}
        return cls.read(session, filter_by=filter_dict)
