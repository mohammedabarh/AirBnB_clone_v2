#!/usr/bin/python3
"""Database storage engine using SQLAlchemy."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

class DBStorage:
    """Database storage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_pre_ping=True)

    def all(self, cls=None):
        """Query all objects from the database."""
        pass

    def new(self, obj):
        """Add a new object to the current session."""
        pass

    def save(self):
        """Commit changes to the database."""
        pass

    def delete(self, obj=None):
        """Delete an object from the current session."""
        pass

    def reload(self):
        """Create all tables in the database and initialize the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.remove()
