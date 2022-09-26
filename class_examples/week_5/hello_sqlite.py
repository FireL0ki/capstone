import sqlite3

conn = sqlite3.connect('first_db.sqlite')  # connect or create new if not exist

conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)') # will take care of error in case code has run and already created table previously

# These rows will be added every time program is run
# conn.execute('INSERT INTO products values (1000, "hat")')
# conn.execute('INSERT INTO products values (1000, "jacket")')
# conn.execute('INSERT INTO products values (1000, "shirt")')

conn.commit() # save to DB

# results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
# first_row = results.fetchone()
# print(first_row)

results = conn.execute('SELECT * FROM products')
for row in results: 
    print(row)

new_id = int(input('Enter a new id: '))
new_name = input('Enter a new product: ')

conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name) )
conn.commit()

conn.close()
