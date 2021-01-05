from sqlitemodel import Model, Database

Database.DB_FILE='/home/msilva/proj/analfiles/data/database.db'

class Arquivo(Model):
    def __init__(self, id=None):
        Model.__init__(self, id, dbfile=None, foreign_keys=False, parse_decltypes=False)
        self.arquivo=''
        self.md5sum=''
        self.data=''
        self.tamanho=0

    def tablename(self):
        return 'arquivos'

    def columns(self):
        return [
            {
                'name': 'arquivo',
                'type': 'TEXT',
            },
            {
                'name': 'md5sum',
                'type': 'TEXT',
            },
            {
                'name': 'data',
                'type': 'DATETIME',
            },
            {
                'name': 'tamanho',
                'type': 'INTEGER',
            }
        ]
