#  app/models.py

import sys

from sqlalchemy import \
    Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import \
    declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            
        }



class Item(Base):
    __tablename__ = 'item'
    name = Column(
        String(80), nullable=False)
    id = Column(
        Integer, primary_key=True
    )
    description = Column(String(350))
    picture = Column(String(350))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        # Return OBJ Data
        return{
            'name': self.name,
            'decription': self.description,
            'picture':self.picture,
            'id': self.id,
        }


engine = create_engine('postgresql+psycopg2://vagrant:vagrant@localhost/catalog')
Base.metadata.create_all(engine)
