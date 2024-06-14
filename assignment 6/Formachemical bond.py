import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Elements (
    symbol VARCHAR PRIMARY KEY,
    type ENUM('Metal', 'Nonmetal', 'Noble'),
    electrons INT
)
''')

elements_data = [
    ('He', 'Noble', 0),
    ('Na', 'Metal', 1),
    ('Ca', 'Metal', 2),
    ('La', 'Metal', 3),
    ('Cl', 'Nonmetal', 1),
    ('O', 'Nonmetal', 2),
    ('N', 'Nonmetal', 3)
]

cursor.executemany('INSERT INTO Elements (symbol, type, electrons) VALUES (?, ?, ?)', elements_data)

query = '''
SELECT e1.symbol AS metal, e2.symbol AS nonmetal
FROM Elements e1, Elements e2
WHERE e1.type = 'Metal' AND e2.type = 'Nonmetal'
'''

cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()