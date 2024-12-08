from database.models.user import User
from database.database import Database


class UserService:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add_user(self, user_id, name, user_name):
        session = Database().get_session()
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if user:
            user.full_name = name
            user.user_name = user_name
        else:
            user = User(telegram_id=user_id,
                        full_name=name, user_name=user_name)
            session.add(user)
        session.commit()

    def get_user(self, user_id):
        session = Database().get_session()
        return session.query(User).filter_by(telegram_id=user_id).first()
