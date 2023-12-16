#!/usr/bin/python3
"""file that contains the class definition of a\
        State and an instance Base = declarative_base()"""
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer


Base = declarative_base()


class State(Base):
    '''creates state'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
