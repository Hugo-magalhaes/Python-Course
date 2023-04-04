import sqlite3
from pathlib import Path

# ! SQLite é bom em ter uma única conexão
# - Dbeaver aplicativo para bases de dados

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR/DB_NAME
TABLE_NAME = 'costumers'

conexao = sqlite3.connect(DB_FILE)

cursor = conexao.cursor()

# cursor.execute(f'DELETE FROM {TABLE_NAME}')

cursor.execute('CREATE TABLE IF NOT EXISTS'
               f' {TABLE_NAME} ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL)'
               )

# cursor.execute(f'INSERT INTO {TABLE_NAME} '
#                '(id, name, weight) '
#                'VALUES '
#                '(NULL, "Maria", 50), '
#                '(NULL, "Hugo", 47), '
#                '(NULL, "João", 68)'
#                )

# - Zera a sequência dos ID's
# cursor.execute(f'DELETE FROM sql_sequence where name="{TABLE_NAME}"')


sql = (f'INSERT INTO {TABLE_NAME} '
       '(id, name, weight) '
       'VALUES '
       '(?, ?, ?)')

# ? Mais seguro
# cursor.execute(sql, ['NULL','joana', 4])
cursor.executemany(sql, [['NULL', 'joana', 4],
                         ['NULL', 'luiz', 20]])

sql1 = (f'INSERT INTO {TABLE_NAME} '
        '(name, weight) '
        'VALUES '
        '(:nome, :peso)')

# cursor.execute(sql, {'nome': 'joana', 'peso': 4})
cursor.executemany(sql1, [
    {'nome': 'joana', 'peso': 4},
    {'nome': 'hugo', 'peso': 2},
    {'nome': 'miguel', 'peso': 3},
])

# cursor.execute('SELECT * FROM clientes')

# cursor.execute('SELECT name, weight FROM clientes WHERE weight > 50')

# ! Delete sempre com where
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': 1})

# cursor.execute('UPDATE clientes SET weight=:weight WHERE id=:id',
#                {'weight': 51, 'id': 2})


conexao.commit()

for i in cursor.fetchall():
    print(i)

cursor.close()
conexao.close()
