#!/usr/bin/python3
"""
Lists all State objects from the db hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    # Launch the engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    # Close the engine
    engine.dispose()
