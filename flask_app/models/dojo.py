from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("ninjas_and_dojos_schema").query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))

        return dojos


    @classmethod
    def create(cls, dojo_name):
        query = f"INSERT INTO dojos (name) VALUES ('{dojo_name}');"
        results = connectToMySQL("ninjas_and_dojos_schema").query_db(query)

        return results


    @classmethod
    def get_one(cls, dojo_name):
        query = f"SELECT * FROM dojos WHERE name = '{dojo_name}';"
        results = connectToMySQL("ninjas_and_dojos_schema").query_db(query)

        dojo = Dojo(results[0])
        dojo.ninjas = Ninja.get_all_in_dojo(dojo_name)

        return dojo