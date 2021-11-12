from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]


    @classmethod
    def create(cls, ninja):
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
                    VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"""

        return connectToMySQL('ninjas_and_dojos_schema').query_db(query, ninja)


    @classmethod
    def get_all_in_dojo(cls, dojo_name):
        query = f"""SELECT dojos.id, first_name, last_name, age, dojo_id 
                    FROM ninjas 
                    LEFT JOIN dojos ON dojos.id = ninjas.dojo_id 
                    WHERE dojos.name = '{dojo_name}';"""

        results = connectToMySQL("ninjas_and_dojos_schema").query_db(query)

        ninjas = []
        for row in results:
            ninjas.append(Ninja(row))

        return ninjas