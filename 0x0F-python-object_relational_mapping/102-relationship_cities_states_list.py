#!/usr/bin/python3
"""Module to list cities"""


from relationship_city import Base, City, State
import sqlalchemy
import sqlalchemy.orm
import sys


def main():
    """List all cities by their state only querying cities"""

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
    query = session.query(City).order_by(City.id)
    for city in query:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))


if __name__ == '__main__':
    main()
