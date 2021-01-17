from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Connection
from enum import Enum
engine = create_engine("mysql+pymysql://admin:admin1234@121.4.203.2:3306/Peppa?charset=utf8")
Session = sessionmaker(bind=engine)
con=Connection(engine)
Base = declarative_base()

class DataType(Enum):
    mssql=1
    mysql=2

class Provider():
    def __init__(self,ConnectionString:str=None):
        self.engine = create_engine(ConnectionString)
        self.Session = sessionmaker(bind=engine)
        self.connection=Connection(engine)
        self.Base = declarative_base()
    def ConnectionString(datatype:DataType,host:str,dbname:str,username:str,password:str,port:int=None):
        dbtype=""
        if datatype== DataType.mssql:
            dbtype="mssql+pymssql"
        elif datatype== DataType.mysql:
            dbtype="mysql+pymysql"
        else:
            dbtype=""
        return "{dbtype}://{username}:{password}@{host}{port}/{dbname}?charset=utf8".format(dbtype=dbtype,username=username,password=password,dbname=dbname,host=host,port=':'+str(port) if port is not None else '')
