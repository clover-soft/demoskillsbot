from database.models.user import User
from database.database import Database


class UserService:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add_user(self, tg_user_id, tg_user_name, tg_user_json):
        session = Database().get_session()
        user = session.query(User).filter_by(tg_user_id=tg_user_id).first()
        if user:
            user.tg_user_name = tg_user_name
            user.tg_user_json = tg_user_json
        else:
            user = User(
                tg_user_id=tg_user_id,
                tg_user_name=tg_user_name,
                tg_user_json=tg_user_json
            )
            session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_user(self, user_id):
        session = Database().get_session()
        return session.query(User).filter_by(telegram_id=user_id).first()
