#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb:/{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sc = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in sc:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
