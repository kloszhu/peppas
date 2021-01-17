from Utils.ConfigPath import ConfigPath
from configparser import ConfigParser
class IniHelper():
    def __init__(self, path: str = None):
        self.IniDbConfig=ConfigPath()
        if path is not None:
            self.DefaultPath=path
        else:
            self.DefaultPath=self.IniDbConfig.DbININame
    def getSection(self, key: str, item: str):
        rc = ConfigParser()
        rc.read(self.DefaultPath,encoding='utf-8')
        return rc[key][item]
    def has_Section(self,secton):
        rc = ConfigParser()
        rc.read(self.DefaultPath,encoding='utf-8')
        return rc.has_section(secton)
    def setSection(self,secton, option, value=None):
        rc = ConfigParser()
        rc.read(self.DefaultPath,encoding='utf-8')
        if  rc.has_section(secton) is not True:
            rc.add_section(secton)
        rc.set(secton, option, value)
        rc.write(open(self.DefaultPath, 'w', encoding='utf-8'))
