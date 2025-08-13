from flask import make_response

def popup_message(message):
    html = f"""
    <script>
        alert("{message}");
        window.history.back(); // volta para a página anterior
    </script>
    """
    return make_response(html, 200)

def render_task_list(task_list):
    html = "<h1>Lista de Tarefas</h1><ul>"
    for tid, task in task_list.items():
        html += f"<li>{tid}: {task['title']} - {'Concluída' if task['done'] else 'Pendente'}</li>"
    html += "</ul>"
    return make_response(html, 200)

def render_task(task):
    if task is None:
        return popup_message("Tarefa não encontrada!")
    html = f"<h1>Detalhes</h1><p>{task}</p>"
    return make_response(html, 200)

def render_created_task(task):
    return popup_message("Tarefa criada com sucesso!")

def render_deleted_task(success):
    if success is None:
        return popup_message("Tarefa não encontrada!")
    return popup_message("Tarefa deletada com sucesso!")

def render_updated_task(success):
    if success is None:
        return popup_message("Tarefa não encontrada!")
    return popup_message("Tarefa atualizada com sucesso!")
