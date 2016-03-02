import sqlite3

with sqlite3.connect('test_database.db') as connection:

    c = connection.cursor()

    c.executescript("""

DROP TABLE IF EXISTS People;

CREATE TABLE People(FirstName TEXT, LASTNAME Text, Age INT);

""")

peopleValues = (

('Ron', 'Obvious', 42),

('Luigi', 'Vercotti', 43),

('Arthur', 'Belling', 28)

)

c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
