import os


class ConfigPath():
    def __init__(self, *args, **kwargs):
        self.basepath=os.getcwd()
        self.DbININame=os.path.join(self.basepath,"database.ini")
        return super().__init__(*args, **kwargs)
