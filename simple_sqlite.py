import sqlite3, db_helper, sys

class connect:
    def __init__(self, database=':memory:'):
        try:
            self.connection = sqlite3.connect(database=database)
        except:
            raise sqlite3.Error('database does not exist -- %s' % (database))
        if database == ':memory:':
            print('Database created in memory.', file=sys.stderr)
        self.cursor = self.connection.cursor()
    
    def query(self, query, arg=(), style='raw'):
        try:
            self.cursor.execute(query, arg)
        except:
            raise sqlite3.Error('Error in syntax:\n\tQuery: %s\n\tArguments: %s' % (query, arg))
        query_split = query.lower().strip().split()
        if query_split[0] in ('show','describe','select'):
            result = self.cursor.fetchall()
            description = self.description()
            if style == 'raw':
                return result
            result = db_helper.make_mapped(description, result)
            if style == 'json-ready':
                return result
            raise Exception('style not supported')
        self.connection.commit()

    def description(self):
        return self.cursor.description

    def __del__(self):
        self.connection.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, key, value, tracepath):
        del self