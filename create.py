
import sqlite3

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
# 		first_name text,
# 		last_name text,
# 		address text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")
# conn.commit()		

c.execute(""" insert into addresses values ('narendra','medisetti','john134','john','john','1234')
		""")
conn.commit()			