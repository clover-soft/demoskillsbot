from database.database import Database
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Date


class User(Database().Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    user_name = Column(String(255))
    full_name = Column(String(255))
    weather_requests = Column(Integer, default=0)
    gpt_requests = Column(Integer, default=0)
    last_reset = Column(Date, default='CURRENT_DATE')

    def __repr__(self):
        return f"User(id={self.id!r}, telegram_id={self.telegram_id!r}, name={self.name!r})"
