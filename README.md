# 🚀Gerenciador de tarefas 

Esse projeto é um gerenciador de tarefas que armazena os dados em um arquivo **JSON**. Que tem as funções básicas como: criar, deletar, modificar, listar. O famoso *CRUD*. Ele utiliza bibliotecas como: `json argparse unittest datetime uuid` entre outros, funções e classes para gerenciar as tarefas do usuário.

# ⚙️Utilizando o script
Você pode utilizar o script dando os seguintes comandos:

## Criar uma tarefa
Esse comando adiciona uma tarefa ao arquivo JSON.
```powershell
python cli.py add "Minha tarefa" "Descrição da tarefa" --status em_progresso
```
Obs. --status é opcional, mas o padrão dele é "pendente".

## Deletar uma tarefa
E esse comando deleta uma tarefa ao arquivo JSON.
```powershell
python cli.py delete <task_id>
```
Obs. *task_id* é retornado pelo add.

## Listar uma tarefa
Esse comando lista todas as tarefas do arquivo JSON e filtra as que apareces.
```powershell
python cli.py list --status em_progresso
```
Obs. --status filtra as tarefas que vão aparecer.

## Modificar uma tarefa
E esse comando modifica uma tarefa já existente no arquivo JSON.
```powershell
python cli.py update <task_id> --title "Minha tarefa finalizada" --status concluido
```
