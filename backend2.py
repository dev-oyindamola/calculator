import sqlite3

def create():
	with sqlite3.connect("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS Base (
				diseases CHAR(40),
				symptoms CHAR(500),
				body CHAR(10000000000000)

			)""")
		connection.commit()

def create_diseases(diseases,symptoms,body):
	with sqlite3.connect("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("""INSERT INTO Base VALUES (?,?,?)""",
			(diseases,symptoms,body))
		connection.commit()

def get_data(diseases):
	with sqlite3.connect("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM Base WHERE diseases=?", (diseases,))
		row = cursor.fetchall()
		connection.commit()
		for ro in row:
			return "".join(ro)

def get_date(symptoms):
	with sqlite3.connect("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM Base WHERE symptoms=?", (symptoms,))
		key = cursor.fetchall()
		connection.commit()
		for r in key:
			return "".join(r)
		

def view_all():
	with sqlite3.connect("data.db") as connection:
		cursor = connection.cursor()
		all_data =cursor.execute("SELECT * FROM Base").fetchall()
		connection.commit()
		return all_data

car = """
bloating,
weakness,
stomach pain,
abdominal pain,
nausea,
headache,
loss of appetite
"""

dog = """
Typhoid is cause by bad water
"""

create()
# print(create_diseases("\n",,dog))
# print(view_all())
# print(get_data("typhoid: "))