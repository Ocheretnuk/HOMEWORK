import sys

from diary import storage
get_connection = lambda: storage.connect('diary.sqlite')

def tasks():
	with get_connection() as conn:
		print(storage.task_all(conn))
		
def tasks_time():
	time = input('\nВведи дату «YYYY.MM.DD»: ')
	with get_connection() as conn:
		print(storage.task_time(conn, time))
		
def tasks_not_complete():
	with get_connection() as conn:
		print(storage.task_shape(conn))
		
def tasks_add():
	name = input('\nвведи имя задачи: ')
	opisane = input('\nо задаче: ')
	time = input('\nдату выполнения  «YYYY.MM.DD»: ')
	with get_connection() as conn:
		print(storage.add(conn, name, opisane, time))
		
def tasks_edit():
	id = input('\nномер задачи: ')
	print('''редактирование:
	1. Изменить название 
	2. Изменить описание
	3. Изменить дату
	4. Изменить статус 
	5. Выход 
	''')		
	
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('введи правильный номер')		
	
	def redact_task_name():
		with get_connection() as conn:
			update_name = input('\nПереименуй задачу: ')
			storage.update_name(conn, id, update_name)
		
		
	def redact_task_opisane():
		with get_connection() as conn:
			update_opisane= input('\nПерепиши описание: ')
			storage.update_opisane(conn, id, update_opisane)
		
		
	def redact_task_time():
		with get_connection() as conn:
			update_time = input('\nВведи новую дату «YYYY.MM.DD»: ')
			storage.update_time(conn, id, update_time)
			
	def redact_task_complete():
		with get_connection() as conn:
			shape = input('\nИзменить статус задачи: ')
			storage.complete(conn, id, shape)
	
		
	edit_actions = {
		'1': redact_task_name,
		'2': redact_task_opisane,
		'3': redact_task_time,
		'4': redact_task_complete,
		'5': main,
	}
	
	while 1:
		cmd = input('\nВведите команду: ')
		action = edit_actions.get(cmd)
		if action:
			action()
		else:
			print('Неизвестная команда')
			
			
def tasks_restart():
	id = input('\nномер задачи?: ')
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('введи правильный номер')
		else:
			storage.restart(conn, id)
			
def tasks_show_menu():
	print('''Выберите действие:
1. Добавить задачу 
2. Редактировать задачу
3. Начать задачу  заново
4. Все задачи
5. Задачи по дате 
6. Вывести список невыполненных задач
m. Показать меню
q. Выйти
''')

def go_away():
	sys.exit(0)

def main():
	with get_connection() as conn:
		storage.initialize(conn)
	tasks_show_menu()
	actions = {
		'1': tasks_add,
		'2': tasks_edit,
		'3': tasks_restart,
		'4': tasks,
		'5': tasks_time,
		'6': tasks_not_complete,
		'm': tasks_show_menu,
		'q': go_away,
	}
	while 1: 
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Неизвестная команда')
	