
# * Como fazer argsparse usar funções do código?
from task_manager import TaskManager
from argparse import ArgumentParser
from pathlib import Path

def main(file_json:Path):
    parser = ArgumentParser(description='Cli gerenciador de tarefas')
    subparsers = parser.add_subparsers(dest='command',required=True)

    add_parser = subparsers.add_parser('add',help='Adiciona uma task')
    add_parser.add_argument('title',help='Titulo da task')
    add_parser.add_argument('description',nargs='?',default='',help='Descrição da task')
    add_parser.add_argument('--status',default='pendente',choices=['pendente','em_progresso','concluido'])

    delete_parser = subparsers.add_parser('delete',help='Deleta uma task')
    delete_parser.add_argument('task_id',help='ID da task')

    list_parser = subparsers.add_parser('list',help='Lista as tasks')
    list_parser.add_argument('--status',help='Filtrar por status da task')

    modify_parser = subparsers.add_parser('update',help='Modifica uma task')
    modify_parser.add_argument('task_id',help='ID da task')
    modify_parser.add_argument('--title',help='Novo título da task')
    modify_parser.add_argument('--description',help='Nova descrição da task')
    modify_parser.add_argument('--status',choices=['pendente','em_progresso','concluido'],help='Novo status para a task')

    args =  parser.parse_args()

    manager = TaskManager(file_json)

    if args.command == 'add':
        uuid = manager.add_task(args.title,args.description,args.status)
        print(f'Task adicionada!, task_id: {uuid}')
    elif args.command == 'delete':
        manager.delete_task(args.task_id)
        print('Task deletada!')
    elif args.command == 'list':
        tasks = manager.list_tasks(args.status)
        for task in tasks:
            print(f'{task['id']} - {task['title']}, {task['status']}')
    elif args.command == 'update':
        manager.modify_task(args.task_id,args.title,args.description,args.status)
        print('Task modificada!')

if __name__ == '__main__':
    main('project/tasks.json')