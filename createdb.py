import sqlite3


DATABASE = 'banco.db'


def get_db_connection():
	conn = sqlite3.connect(DATABASE)
	conn.row_factory = sqlite3.Row
	return conn


def create_database():
	conn = get_db_connection()
	conn.execute('''
		CREATE TABLE IF NOT EXISTS note (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			title TEXT NOT NULL,
			content TEXT NOT NULL
		)
	''')
	conn.commit()
	conn.close()


if __name__ == '__main__':
	create_database()
