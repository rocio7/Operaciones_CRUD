from mysqlconection import connectToMySQL
class User:
    def __init__(self,data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name =data ['last_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod

    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuario1').query_db(query)
        # [
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        # ]

        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod 
    def guardar(cls,formulario):
        #data ={"first_name":"C", "last_name":"x", "email":"cd@gmail.com"}
        query ="INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('esquema_usuario1').query_db(query,formulario)
        return result

    @classmethod
    def borrar(cls,formulario):
        #formulario= id :1
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuario1').query_db(query,formulario)
        return result

    @classmethod
    def mostrar(cls,formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuario1').query_db(query,formulario)
        # [
        #     {'3','Juana','De Arco','juana@codingdojo.com','2022-03-09 14:50:58','2022-03-09 14:50:58'}
        # ]
        usr = result[0]
        user = cls(usr)
        return user 

    @classmethod 
    def actualizar(cls,formulario):
        #formulario = {"id":1, first_name":"c" "last_name":"X","email": "cd@com"}
        query= "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result=connectToMySQL('esquema_usuario1').query_db(query,formulario)
        return result


    

