from flask import Flask
from controllers.task_controller import task_bp

app = Flask(__name__)

# Registra as rotas do controlador de tarefas
app.register_blueprint(task_bp, url_prefix="/tasks")

if __name__ == "__main__":
    app.run(debug=True)
