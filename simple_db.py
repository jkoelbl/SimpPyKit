class database:
    def __init__(self, config, db_type):
        self.connection = db_type.connect(**config)
        self.cursor = self.connection.cursor()
    
    def query(self, query, arg=()):
        self.cursor.execute(query, arg)
        query_split = query.lower().strip().split()
        if query_split[0] in ('show','describe','select'):
            return self.cursor.fetchall()
        self.connection.commit()

    def description(self):
        return self.cursor.description

    def __del__(self):
        self.connection.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, key, value, tracepath):
        del self