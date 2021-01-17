
#from sqlalchemy import create_engine
#import pymysql
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
#postgresql+psycopg2://@localhost/test
#mysql+mysqldb://@localhost/test
import os
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Connection
mysql="mysql+pymysql://admin:admin1234@121.4.203.2:3306/Peppa?charset=utf8"
mssql="mssql+pymssql://sa:sa123456@127.0.0.1/it_db?charset=utf8"
engine = create_engine(mssql)
Session = sessionmaker(bind=engine)
con=Connection(engine)
Base = declarative_base()

def Search(con:Connection):
    mysqlstr="select * from person where 1=1 "
    mssqlstr="""
    SELECT [uid]
      ,[status]
      ,[name]
      ,[sid]
      ,[roles]
      ,[createdate]
      ,[updatedate]
      ,[altuid]
      ,[password]
      ,[gid]
      ,[environ]
      ,[hasdbaccess]
      ,[islogin]
      ,[isntname]
      ,[isntgroup]
      ,[isntuser]
      ,[issqluser]
      ,[isaliased]
      ,[issqlrole]
      ,[isapprole]
  FROM [dbo].[sys_users] where uid in :uid
    """
    cursor = con.execute(text(mssqlstr),{'uid': [1,2,9]})
    result = cursor.fetchall()
    print(type(result))
    print(result)
    for x in result:
        print(x)

def Insert(con:Connection):
    sql="""  
    INSERT INTO person (`name`,age,sex ) VALUES(:name,:age,:sex)
    """
    con.execute(text(sql),{'name':'这是一个','age':18,'sex':'男'})


Search(con)
#Insert(con)


from enum import Enum

class DataType(Enum):
    mssql=1
    mysql=2

def ConnectionString(datatype:DataType,host:str,dbname:str,username:str,password:str,port:int=None):
    dbtype=""
    if datatype== DataType.mssql:
        dbtype="mssql+pymssql"
    elif datatype== DataType.mysql:
        dbtype="mysql+pymysql"
    else:
        dbtype=""
    return "{dbtype}://{username}:{password}@{host}{port}/{dbname}?charset=utf8".format(dbtype=dbtype,username=username,password=password,dbname=dbname,host=host,port=':'+str(port) if port is not None else '')


print(ConnectionString(DataType.mssql,"127.0.0.1","it_db","sa","sa123456"))

print(ConnectionString(DataType.mysql,"121.4.203.2","Peppa","admin","admin1234",3306))
print(os.getcwd())