
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Connection
from DataAccess.DbConfig import DbConfig
engine = create_engine("mysql+pymysql://admin:admin1234@121.4.203.2:3306/Peppa?charset=utf8")
Session = sessionmaker(bind=engine)
con=Connection(engine)
Base = declarative_base()

class Repository():
    def __init__(self,ConnectionString:str=None):
        if ConnectionString is not None:
            self.engine = create_engine(ConnectionString)
        self.engine = create_engine(DbConfig().getDbConnectionStr())
        self.Session = sessionmaker(bind=engine)
        self.connection=Connection(engine)
        self.Base = declarative_base()
    def QueryList(AllSql:str,parampters=None):
        cursor = con.execute(text(AllSql),parampters)
        return cursor.fetchall()
    def First(AllSql:str,parampters=None):
        cursor = con.execute(text(AllSql),parampters)
        return cursor.()

    