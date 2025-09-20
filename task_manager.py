# * Tera que abrir o arquivo em todas as funções?
# Tera que savar os arquivos em todas as funções?.
# * Como fazer isso -> "2025-09-16T19:14:00"?
from storage import save_data,get_data
from datetime import datetime
from typing import Literal
from uuid import uuid4,UUID
from pathlib import Path

class TaskManager:
    def __init__(self,file_json:Path):
        self.file_json = file_json
        self.tasks = get_data(self.file_json)

    def add_task(self,title:str,description:str,status:Literal['pendente','em_progresso','concluido'] = 'pendente') -> UUID:

        # * Verificação de entradda (Input) --------------------------------------------------------------
        if not isinstance(title,str):
            raise TypeError(f'Tipo de valor inválido: "{type(title)}", tipo do valor esperado: "str"')
        if not isinstance(description,str):
            raise TypeError(f'Tipo de valor inválido: "{type(description)}", tipo do valor esperado: "str"')
        if not isinstance(status,str):
            raise TypeError(f'Tipo de valor inválido: "{type(status)}", tipo do valor esperado: "str"')
        if status not in ('pendente','em_progresso','concluido'):
            raise ValueError(f'Valor do status inválido: "{status}"')
        # * --------------------------------------------------------------------------------------------
        
        uuid = str(uuid4())

        self.tasks.append({
            'id':uuid,
            'title':title,
            'description':description,
            'status':status,
            'create_at':datetime.now().isoformat()
        })
        save_data(self.tasks,self.file_json)
        return uuid

    def delete_task(self,task_id:str):

        # * Verificação de entradda (Input) --------------------------------------------------------------
        if not isinstance(task_id,str):
            raise TypeError(f'Tipo de valor inválido: "{type(status)}", tipo do valor esperado: "str"')
        # * --------------------------------------------------------------------------------------------
        non_task_id = []
        index_del_task = None
        for task in self.tasks:
            if task['id'] == task_id:
                index_del_task = self.tasks.index(task)
                break
            else:
                non_task_id.append(task)
        if len(non_task_id) == len(self.tasks):
            raise ValueError('ID da task não encontrado, ou inválido')
        self.tasks.pop(index_del_task)
        save_data(self.tasks,self.file_json)
    
    def list_tasks(self,status:Literal['todos','pendente','em_progresso','concluido'] = 'todos'):

        # * Verificação de entradda (Input) --------------------------------------------------------------
        if status:
            if status not in ('todos','pendente','em_progresso','concluido'):
                raise ValueError(f'Valor do status inválido: "{status}"')
            if not isinstance(status,str):
                raise TypeError(f'Tipo de valor inválido: "{type(status)}", tipo do valor esperado: "str"')
        else:
            status = 'todos'
        # * --------------------------------------------------------------------------------------------
        tasks = []
        for task in self.tasks:
            if status == 'todos':
                tasks.append(task)
            else:
                if status == task['status']:
                    tasks.append(task)

        return tasks

    def modify_task(self,task_id:str,title:str=None,description:str=None,status:Literal['pendente','em_progresso','concluido']=None):

        # * Verificação de entradda (Input) --------------------------------------------------------------
        if not isinstance(title,str) and title:
            raise TypeError(f'Tipo de valor inválido: "{type(title)}", tipo do valor esperado: "str"')
        if not isinstance(description,str) and description:
            raise TypeError(f'Tipo de valor inválido: "{type(description)}", tipo do valor esperado: "str"')
        if not isinstance(status,str) and status:
            raise TypeError(f'Tipo de valor inválido: "{type(status)}", tipo do valor esperado: "str"')
        if status not in ('pendente','em_progresso','concluido') and status:
            raise ValueError(f'Valor do status inválido: "{status}"')
        # * --------------------------------------------------------------------------------------------
        
        non_task_id = []
        for task in self.tasks:
            if task['id'] == task_id:
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if status:
                    task['status'] = status
            else:
                non_task_id.append(task)
            
        if len(non_task_id) == len(self.tasks):
            raise ValueError('ID da task não encontrado, ou inválido')
        
        save_data(self.tasks,self.file_json)

    def get_task(self,task_id:str):

        # * Verificação de entradda (Input) --------------------------------------------------------------
        if not isinstance(task_id,str):
            raise TypeError(f'Tipo de valor inválido: "{type(task_id)}", tipo do valor esperado: "str"')
        # * --------------------------------------------------------------------------------------------

        for task in self.tasks:
            if task['id'] == task_id:
                return task

if __name__ == '__main__':
    task = TaskManager('project/tasks.json')