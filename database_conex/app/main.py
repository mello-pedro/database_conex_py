from class_conex import Conex_database

## Conectar ao database usando a Class Conex_database (colocar senha no lugar do xxxxxxxxx)
conectar = Conex_database('localhost', '5XXX', 'YOURDBNAMEHERE', 'YOURDBUSERHERE', 'DBPASSWORDHERE')
conectar.connexion()

## Fazer a query e guardar os resultados em uma variavel result
result = conectar.cursor_conex('SELECT * FROM orders LIMIT 10')

## Salvar o dataframe na minha área de trabalho
conectar.save_dataframe(result, '/Users/northwind_test.csv')
conectar.close_conn()