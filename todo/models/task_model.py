# Banco de dados em memória (dicionário)
tasks = {
    1: {"title": "Comprar leite", "done": False},
    2: {"title": "Estudar Flask", "done": True}
}

def get_all_tasks():
    return tasks

def get_task(task_id):
    return tasks.get(task_id)

def add_task(title):
    new_id = max(tasks.keys()) + 1 if tasks else 1
    tasks[new_id] = {"title": title, "done": False}
    return {new_id: tasks[new_id]}

def update_task(task_id, title=None, done=None):
    if task_id not in tasks:
        return None
    if title is not None:
        tasks[task_id]["title"] = title
    if done is not None:
        tasks[task_id]["done"] = done
    return {task_id: tasks[task_id]}

def delete_task(task_id):
    return tasks.pop(task_id, None)
