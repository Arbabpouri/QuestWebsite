from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Database:

    def __init__(self) -> None:
        self.__engine = create_engine('sqlite:///database.db')
        self.session = sessionmaker(bind=self.__engine)()

    def create_all_table(self) -> bool:
        try:
            Base.metadata.create_all(self.__engine)
            return True
        except:
            return False


class QuestsAndAnswers(Base):
    __tablename__ = "answers"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quest_1 = Column("quest_1", String(300), nullable=False)
    quest_2 = Column("quest_2", Integer(), nullable=False)
    quest_3 = Column("quest_3", Integer(), nullable=False)
    quest_4 = Column("quest_4", String(150), nullable=True, default=None)
    quest_5 = Column("quest_5", String(30), nullable=True, default=None)
    quest_6 = Column("quest_6", Integer(), nullable=False)
    quest_7 = Column("quest_7", Integer(), nullable=False)
    quest_8 = Column("quest_8", String(150), nullable=False)
    quest_9 = Column("quest_9", Integer(), nullable=False)
    quest_10 = Column("quest_10", Integer(), nullable=False)
    quest_11 = Column("quest_11", Integer(), nullable=False)
    quest_12 = Column("quest_12", String(30), nullable=False)


if __name__ == "__main__":

    Database().create_all_table()
