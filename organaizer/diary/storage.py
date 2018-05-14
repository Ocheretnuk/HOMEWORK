import os.path as Path
import sqlite3

SQL_INSERT_TASK = 'INSERT INTO diary (name, opisane, time) VALUES (?,?,?)'

SQL_UPDATE_TASK_NAME = '''
    UPDATE diary SET name=? WHERE id=?
'''

SQL_UPDATE_TASK_OPISANIE = '''
    UPDATE diary SET opisane=? WHERE id=?
'''

SQL_UPDATE_TASK_TIME = '''
    UPDATE diary SET time=? WHERE id=?
'''

SQL_UPDATE_TASK_SHAPE = '''
    UPDATE diary SET shape=? WHERE id=?
'''

SQL_SELECT_ALL = '''
    SELECT 
        id, name, opisane, time, shape
    FROM 
		diary 
'''

SQL_SELECT_TASK_BY_SHAPE = SQL_SELECT_ALL + ' WHERE shape=?'
SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'
SQL_SELECT_TASK_BY_TIME = SQL_SELECT_ALL + ' WHERE time=?'

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn

def initialize(conn):
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())
		
def task_all(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL)
		return cursor.fetchall()

def task_time(conn, time):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_TIME, (time,))
		return cursor.fetchall()

def task_one(conn, id):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (id,))
		return cursor.fetchone()

def task_shape(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_SHAPE, ('ne_sdelano',))
		return cursor.fetchall()

def add(conn, name, opisane, time):
	if not name:
		raise RuntimeError("Task name can't be empty.")
		
	with conn:
		cursor = conn.execute(SQL_INSERT_TASK, (name, opisane, time,))
		pk = cursor.lastrowid
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
		return cursor.fetchone()
		
def complete(conn, id, shape):
	with conn:
		conn.execute(SQL_UPDATE_TASK_SHAPE, (shape, id,))
		
		
def restart(conn, id):
	with conn:
		cursor = conn.execute(SQL_UPDATE_TASK_SHAPE, ('ne_sdelano', id,))
	
		
def update_name(conn, id, name):
	if not name:
		raise RuntimeError("Task name can't be empty.")
		
	with conn:
		conn.execute(SQL_UPDATE_TASK_NAME, (name, id,))
		
def update_opisane(conn, id, opisane):
	with conn:
		conn.execute(SQL_UPDATE_TASK_OPISANIE, (opisane, id,))
			
def update_time(conn, id, time):
	with conn:
		conn.execute(SQL_UPDATE_TASK_TIME, (time, id,))
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		

