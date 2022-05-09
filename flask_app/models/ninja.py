from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create(cls, data):
        print('inserting ninja into db...')
        query = 'insert into ninjas (first_name, last_name, age, dojo_id) values ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all(cls):
        query = 'select * from ninjas'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for n in results:
            ninjas.append(Ninja(n))
        return ninjas

    @classmethod
    def get_ninjas_by_dojo_id(cls, data):
        print('getting ninjas by id...')
        query = """select first_name, last_name, age, dojo_id, ninjas.created_at, ninjas.updated_at, name  
                     from ninjas
                     join dojos
                       on ninjas.dojo_id = dojos.id
                    where dojo_id = %(id)s;"""
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_by_id(cls):
        pass

    @classmethod
    def edit(cls):
        pass

    @classmethod
    def delete(cls):
        pass