import os
import json

def listar(task_list):
	print('-'*10)
	if not task_list:
		print('Lista de tarefas vazia.')
		print('-'*10)
		return
	print('TAREFAS:')
	for task in task_list:
		print(task)
	print('-'*10)

def desfazer(task_list, deleted_task):
	if not task_list:
		print('-'*10)
		print('Nada para ser desfeito.')
		print('-'*10)
		return
	
	deleted_task.append(task_list.pop())
	listar(task_list)

def refazer(task_list, deleted_tasks):
	if not deleted_tasks:
		print('-'*10)
		print('Nada para ser refeito.')
		print('-'*10)
		return
	
	task_list.append(deleted_tasks.pop())
	listar(task_list)

def adicionar(task, task_list):
	task_list.append(task)
	listar(task_list)

def ler(tasks, file_path):
	datas = []
	try:
		with open(file_path, 'r', encoding='utf8') as file:
			datas = json.load(file)
	except FileNotFoundError:
		print('Arquivo não exsite')
		salvar(tasks, file_path)
	return datas

def salvar(tasks, file_path):
	datas = tasks
	with open(file_path, 'w', encoding='utf8') as file:
		datas = json.dump(tasks, file, indent=2, ensure_ascii=False)
	return datas

FILE_PATH = 'aula119.json'
deleted_item_list = []
task_list = ler([], FILE_PATH)

while True:
	print('Comandos: listar | desfazer | refazer')
	client_task = input('Digite uma tarefa ou comando: ')

	comandos = {
		'listar': lambda: listar(task_list),
		'desfazer': lambda: desfazer(task_list, deleted_item_list),
		'refazer': lambda: refazer(task_list, deleted_item_list),
		'clear': lambda: os.system('cls'),
		'adicionar': lambda: adicionar(client_task, task_list),
	}

	comando = comandos.get(client_task) if comandos.get(client_task) is not None \
	else comandos['adicionar']

	comando()
	salvar(task_list, FILE_PATH)

	# if client_task.lower() == 'listar':
	# 	listar(task_list)
	# elif client_task.lower() == 'desfazer':
	# 	desfazer(task_list, deleted_item_list)
	# 	listar(task_list)
	# elif client_task.lower() == 'refazer':
	# 	refazer(task_list, deleted_item_list)
	# 	listar(task_list)
	# elif client_task.lower() == 'clear':
	# 	os.system('cls')
	# else:
	# 	adicionar(client_task, task_list)
		



	

