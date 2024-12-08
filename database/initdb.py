from database.database import Database
from database.models.user import User
from sqlalchemy.engine.reflection import Inspector


class InitDB:
    @staticmethod
    def init_db():
        engine = Database().engine
        inspector = Inspector.from_engine(engine)
        if 'users' not in inspector.get_table_names():
            User.__table__.create(Database().engine)
