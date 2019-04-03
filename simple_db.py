class database:
    def __init__(self, config, db_type):
        self.connection = db_type.connect(**config)
        self.cursor = self.connection.cursor()
    
    def query(self, query, arg=(), value='all'):
        self.cursor.execute(query, arg)
        query_split = query.lower().strip().split()
        if query_split[0] in ('show','describe','select'):
            if value not in ('all', 'one', 'none'):
                raise ValueError('value not valid -- %s' % (value))
            if value == 'all':
                return self.cursor.fetchall()
            if value == 'one':
                return self.cursor.fetch()
            if value == 'none':
                return None
        self.connection.commit()

    def description(self):
        return self.cursor.description
    
    def __iter__(self):
        return self.cursor.fetchall()

    def __next__(self):
        return self.cursor.fetch()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, key, value, tracepath):
        del self