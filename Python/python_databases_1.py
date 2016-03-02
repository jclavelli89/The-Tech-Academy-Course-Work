import sqlite3

connection = sqlite3.connect("test_database.db")

c = connection.cursor()

# Create table
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

# Enter Data
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

# Commit the data
connection.commit()

# Drop table
c.execute("DROP TABLE IF EXISTS People")
