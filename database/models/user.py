from database.database import Database
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.types import JSON
from datetime import datetime
import json


class User(Database().Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_user_id = Column(Integer, unique=True)
    tg_user_name = Column(String(255))
    tg_user_json = Column(JSON)
    local_user_json = Column(JSON)
    inserted_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())

    @property
    def tg_user_json_dict(self):
        return json.loads(self.tg_user_json)

    def __repr__(self):
        return f"User(id={self.id}, tg_user_id={self.tg_user_id}, tg_user_name={self.tg_user_name})"
