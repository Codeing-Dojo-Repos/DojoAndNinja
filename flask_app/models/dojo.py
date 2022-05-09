from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = 'insert into dojos (name) values ( %(name)s )'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = 'select * from dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append( Dojo(d) )
        return dojos

    @classmethod
    def get_by_id(cls):
        pass

    @classmethod
    def edit(cls):
        pass

    @classmethod
    def delete(cls):
        pass