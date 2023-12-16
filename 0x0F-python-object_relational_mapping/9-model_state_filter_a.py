#!/usr/bin/python3
'''script that lists all State objects from the database hbtn_0e_6_usa
'''
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print("{}: {}".format(item.id, item.name))
    session.close()
