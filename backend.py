import sqlite3


def create():
	with sqlite3.connect("databace.db") as connection:
		cursor = connection.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS Password (
				id INTEGER PRIMARY KEY,
				fistename CHAR(50),
				lastname CHAR(20),
				num INTEGER(11),
				user CHAR(20),
				password CHAR(15),
				code CHAR(7)	
				

			)""")
		connection.commit()

def create_password(fistename,lastname,num,user,password,code):
	with sqlite3.connect("databace.db") as connection:
		# connection = connection.connect("databace.db")
		cursor = connection.cursor()
		cursor.execute("""INSERT INTO Password VALUES (NULL,?,?,?,?,?,?)""",
			(fistename,lastname,num,user,password,code))
		connection.commit()
	# connection.close()

def view_all():
	with sqlite3.connect("databace.db") as connection:
		cursor = connection.cursor()
		all_data = cursor.execute("""SELECT * FROM Password"""
			).fetchall()
		connection.commit()
		return all_data

def get_data(num,password):
	with sqlite3.connect("databace.db") as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT num , password FROM Password WHERE num=? AND password=?",(num, password))
		row = cursor.fetchall()
		connection.commit()
		for r in row:
			return r




create()
print(view_all())
# print(get_data("07040221964","oreoluwa"))