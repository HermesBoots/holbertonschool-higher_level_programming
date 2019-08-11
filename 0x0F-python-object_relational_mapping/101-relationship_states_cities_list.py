#!/usr/bin/python3
"""Module to create a city and state"""


from relationship_city import Base, State
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
    rows = session.query(State).order_by(State.id)
    for state in rows:
        print(str(state.id) + ': ' + state.name)
        for city in state.cities:
            print('    ' + str(city.id) + ': ' + city.name)


if __name__ == '__main__':
    main()
