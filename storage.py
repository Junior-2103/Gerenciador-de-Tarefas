# * Como deixar uma lista no JSON e adicionar as coisas nela?
# * Como adicionar a task ao JSON (dentro das chaves)?

from typing import Dict,List
from pathlib import Path
import json
def get_data(path:Path) -> list:
    try:
        with open(path,'r',encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return []
    except FileNotFoundError:
        with open(path,'w') as file:
            return []
def save_data(new_tasks:List[Dict[str,str]],path:Path) -> None:
    with open(path,'w') as file:
        json.dump(new_tasks,file)

if __name__ == "__main__":
    print(get_data('tasks.json'))
    # save_data([{
    #     "id":"tg78rfwtgggf0gu4ep9qayhuqa",
    #     "title":"Comprar leite",
    #     "description":"Comprar leite no mercado Verona ás 16:00",
    #     "create_at":"19-09-2025T19:05:00"
    # }])