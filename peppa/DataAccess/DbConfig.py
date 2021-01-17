from Utils.IniHelper import IniHelper
from enum import Enum


class DbConfig():
    #ini:IniHelper=IniHelper()
    secton="database"
    def __init__(self, *args, **kwargs):
        self.ini:IniHelper=IniHelper()
        return super().__init__(*args, **kwargs)

    def setDbConnectionStr(self,datatype:str,host:str,dbname:str,username:str,password:str,port:int=None):
        
        self.ini.setSection(self.secton,"datatype",datatype)
        self.ini.setSection(self.secton,"host",host)
        self.ini.setSection(self.secton,"dbname",dbname)
        self.ini.setSection(self.secton,"username",username)
        self.ini.setSection(self.secton,"password",password)
        if port is not None:
            self.ini.setSection(self.secton,"port",port if not None else " ")
        self.ini.setSection(self.secton,"connectString",self.ConnectionString(datatype,host,dbname,username,password,port))

    def getDbConnectionStr(self):
        if self.ini.has_Section(self.secton) is not True:
            return None
        return self.ini.getSection(self.secton,"connectString")


    def ConnectionString(self,datatype:str,host:str,dbname:str,username:str,password:str,port:int=None):
        dbtype=""
        if datatype== "mssql":
            dbtype="mssql+pymssql"
        elif datatype== "mysql":
            dbtype="mysql+pymysql"
        else:
            dbtype=""
        return "{dbtype}://{username}:{password}@{host}{port}/{dbname}?charset=utf8".format(dbtype=dbtype,username=username,password=password,dbname=dbname,host=host,port=':'+str(port) if port is not None else '')


cfg=DbConfig()
cfg.setDbConnectionStr("mssql","127.0.0.1","it_db","sa","sa123456")
print(cfg.getDbConnectionStr())
