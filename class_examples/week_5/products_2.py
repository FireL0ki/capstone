import sqlite3

# validation errors, rowid

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    # conn.execute('DROP TABLE products')
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'scarf'
quantity = 10

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity) )
    conn.close()
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM products')
for row in results:
    print(row)

print('End of program!')