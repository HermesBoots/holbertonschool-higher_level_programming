#!/usr/bin/python3
"""Module to create a city and state"""


from model_city import Base, City, State
import sqlalchemy
import sqlalchemy.orm
import sys


def main():
    """Create California and a new city within it"""

    if len(sys.argv) < 4:
        sys.exit(1)
    engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    newState = State(name='California')
    newCity = City(name='San Francisco', state=newState)
    session.add(newCity)
    session.commit()


if __name__ == '__main__':
    main()
