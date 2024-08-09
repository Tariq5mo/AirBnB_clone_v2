#!/usr/bin/python3
"""Module for engine of database
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """Engine of database
    """
    __engine = None
    __session = None

    def __init__(self):
        """The constructor.
        """
        from models.place import Place

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session ('self.__session')
        all objects depending of the class name (argument 'cls')

        Args:
            cls (class instance, optional): all objects depending on it.
            Defaults to None.
        """
        from models.place import Place

        li = []
        if cls is None:
            for subclass in Base.__subclasses__():
                li.extend(self.__session.query(subclass).all())
        else:
            if isinstance(cls, str):  # To convert cls to object if string.
                try:
                    cls = globals()[cls]
                except Exception:
                    pass
            if issubclass(cls, Base):
                li = (self.__session.query(cls).all())
        di = {}
        for obj in li:
            # key be <class-name>.<object-id>
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            try:
                del obj._sa_instance_state
                di[key] = obj
            except Exception:
                pass
        return di

    def new(self, obj):
        """Add the object to the current database session (`self.__session`)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session(self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None.

        Args:
            obj (class_type, optional): The object which will be deleted.
            Defaults to None.
        """
        if obj is not None and issubclass(obj.__class__.__name__, Base):
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database.
        Create the current database session(self.__session).
        """
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped = scoped_session(ses)
        self.__session = scoped

    def close(self):
        """call remove() method on the private session attribute.
        """
        self.__session.remove()
