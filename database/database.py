from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import Config
import logging
import json


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.Base = declarative_base()
            cls._instance._database_uri = Config().get_config_item('DB_URI')
            cls._instance.engine = create_engine(cls._instance._database_uri)
            cls._instance._session = sessionmaker(bind=cls._instance.engine)
            cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def alive_connection(self):
        try:
            self.logger.info("Checking database connection")
            query = text("select 1")
            self._session().execute(query)
            self.logger.info("Database connection is alive")
        except Exception as e:
            self.logger.info(f"Failed to connect to database: {e}")
            self.engine = create_engine(self._database_uri)
            self._session = sessionmaker(bind=self.engine)
            self.logger.info("Reconnected to database")

    def get_session(self):
        self.alive_connection()
        return self._session()
