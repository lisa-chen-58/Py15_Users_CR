from flask_app.config.mysqlconnection import connectToMySQL

# user.py


class User:
    db = "users_cr"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # user.py...
    # gets all the users and returns them in a list of user objects .

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in users_from_db:
            users.append(cls(user))
        return users

    # user.py...
    # gets all the users and returns them in a list of user objects .

    @classmethod
    def save(cls, data):
        query = "Insert INTO users (first_name,last_name,email,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id
