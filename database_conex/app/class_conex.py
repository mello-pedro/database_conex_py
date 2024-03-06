import psycopg2
import csv

class Conex_database:
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None

    def connexion(self):
        try:
            print('conectando ao banco de dados...')
            self.conn = psycopg2.connect(
                host = self.host,
                port =self.port,
                database = self.database,
                user = self.user,
                password = self.password
            )
            print('conexão bem sucedida!')
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados: ", e)

    def cursor_conex(self, query: str):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            results = self.cur.fetchall()
            return results
        except psycopg2.Error as e:
            print("Erro ao executar a query: ", e)
        finally:
            self.close_cur()

    def save_dataframe(self, results, data_path: str):
        try:
            with open(data_path, "w", newline="") as f:
                # Criar o csv
                writer = csv.writer(f)
                writer.writerow([col[0] for col in self.cur.description])
                writer.writerows(results)
                print(f'dados exportados com sucesso para {data_path}')
        except IOError as e:
            print('A exportação falhou!', e)

    def close_cur(self):
        if self.cur:
            self.cur.close()

    def close_conn(self):
        if self.conn:
            self.conn.close()
            print('Conexão fechada com sucesso!')