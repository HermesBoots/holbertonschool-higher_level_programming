#!/usr/bin/python3
"""Module for State class"""


import sqlalchemy
import sqlalchemy.ext.declarative


Base = sqlalchemy.ext.declarative.declarative_base()


class State (Base):
    """A U.S. state stored in a database

    Attributes:
        id (int): a unique ID for this record
        name (str): name of the state

    """

    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(256), nullable=False)
