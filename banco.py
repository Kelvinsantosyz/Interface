import mysql.connector


class DatabaseConnection:
    database_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '305614',
        'database': 'login_dados',
        'auth_plugin': 'mysql_native_password'
    }

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                **self.database_config
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida!")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executada com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao executar a query: {e}")


    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

#CRUD
class UserDados:
    def __init__(self, id_usuario=None):
        self.db = DatabaseConnection()
        self.id_usuario = id_usuario
        self.nome = ""
        self.telefone = ""
        self.email = ""
        self.usuario = ""
        self.senha = ""

    def create_user(self):#CREATE
        query = f"INSERT INTO usuarios (nome, telefone, email, usuario, senha) VALUES ('{self.nome}', '{self.telefone}', '{self.email}', '{self.usuario}', '{self.senha}')"
        self.db.execute_query(query)
        print("Usuário cadastrado com sucesso!")

    def update_user(self):#UPDATE
        try:
            query = f"""UPDATE usuarios SET 
                            nome='{self.nome}',
                            telefone='{self.telefone}',
                            email='{self.email}',
                            usuario='{self.usuario}',
                            senha='{self.senha}'
                        WHERE id={self.id_usuario};"""
            self.db.execute_query(query)
            return "Usuário atualizado com sucesso!"
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar usuário: {e}")
            return "Ocorreu um erro na alteração do usuário"

    def delete_user(self):#DELETE
        try:
            query = f"DELETE FROM usuarios WHERE id={self.id_usuario}"
            self.db.execute_query(query)
            return "Usuário deletado com sucesso!"
        except mysql.connector.Error as e:
            print(f"Erro ao deletar usuário: {e}")
            return "Ocorreu um erro na deleção do usuário"
    def selectUser(self, idusuario):
        try:
            self.db.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (idusuario,))
            resultado = self.db.cursor.fetchone()
            if resultado:
                self.idusuario = resultado[0]
                self.nome = resultado[1]
                self.telefone = resultado[2]
                self.email = resultado[3]
                self.usuario = resultado[4]
                self.senha = resultado[5]
                return "Busca feita com sucesso!"
            else:
                return "Usuário não encontrado."
        except mysql.connector.Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return "Ocorreu um erro na busca do usuário"

