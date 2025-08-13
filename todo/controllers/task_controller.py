from flask import Blueprint, request
from models.task_model import get_all_tasks, get_task, add_task, update_task, delete_task
from views.task_view import render_task_list, render_task, render_created_task, render_deleted_task, popup_message

task_bp = Blueprint("task_bp", __name__)

# GET - listar todas as tarefas
# Teste com curl http://127.0.0.1:5000/tasks/
@task_bp.route("/", methods=["GET"])
def list_tasks():
    return render_task_list(get_all_tasks())

# GET - pegar uma tarefa específica
# Teste com curl http://127.0.0.1:5000/tasks/<id da tarefa>
@task_bp.route("/<int:task_id>", methods=["GET"])
def get_one_task(task_id):
    return render_task(get_task(task_id))

# POST - criar nova tarefa
# Teste com curl -X POST -H "Content-Type: application/json" \ -d '{"title": "Ir à academia"}' \ http://127.0.0.1:5000/tasks/
@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    return render_created_task(add_task(data.get("title")))

# PUT - atualizar tarefa
# Teste com curl -X PUT -H "Content-Type: application/json" \ -d '{"done": true}' \ http://127.0.0.1:5000/tasks/1
@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_one_task(task_id):
    data = request.get_json()
    return render_task(update_task(task_id, data.get("title"), data.get("done")))

# DELETE - remover tarefa
# Teste com curl -X DELETE http://127.0.0.1:5000/tasks/<id da tarefa>
@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_one_task(task_id):
    return render_deleted_task(delete_task(task_id))

# GET via URL para inserir tarefa
# Testar na URL http://127.0.0.1:5000/tasks/add?title=Ir+à+academia
@task_bp.route("/add", methods=["GET"])
def add_task_via_url():
    # Pega o título da query string, ex: /tasks/add?title=NovaTarefa
    title = request.args.get("title")
    if not title:
        return popup_message("Você precisa passar um título!")
    
    # Chama a função do model
    add_task(title)
    
    # Mensagem de sucesso
    return popup_message(f"Tarefa '{title}' criada com sucesso!")

