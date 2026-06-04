from flask import Flask, request, redirect, url_for, render_template_string
from models import TaskManager

PAGE = """<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Список задач</title>
  <style>
    body { font-family: sans-serif; max-width: 520px; margin: 40px auto; }
    form.add { display: flex; gap: 8px; margin-bottom: 16px; }
    form.add input { flex: 1; padding: 8px; }
    ul { list-style: none; padding: 0; }
    li { display: flex; align-items: center; gap: 8px; padding: 6px 0;
         border-bottom: 1px solid #eee; }
    li.done span.text { text-decoration: line-through; color: #999; }
    li span.text { flex: 1; }
    button { cursor: pointer; }
  </style>
</head>
<body>
  <h1>Список задач</h1>
  <form class="add" method="post" action="{{ url_for('add') }}">
    <input name="title" placeholder="Новая задача" autofocus>
    <button type="submit">Добавить</button>
  </form>
  <p>Активных задач: {{ active }}</p>
  <ul>
    {% for task in tasks %}
    <li class="{{ 'done' if task.done else 'active' }}">
      <span class="text">{{ task.title }}</span>
      {% if not task.done %}
      <form method="post" action="{{ url_for('complete', task_id=task.id) }}">
        <button title="Выполнить">&#10003;</button>
      </form>
      {% endif %}
      <form method="post" action="{{ url_for('delete', task_id=task.id) }}">
        <button title="Удалить">&#10007;</button>
      </form>
    </li>
    {% endfor %}
  </ul>
</body>
</html>"""


def create_app():
    app = Flask(__name__)
    app.config["manager"] = TaskManager()

    @app.route("/")
    def index():
        manager = app.config["manager"]
        return render_template_string(
            PAGE, tasks=manager.all_tasks(), active=manager.active_count()
        )

    @app.route("/add", methods=["POST"])
    def add():
        title = request.form.get("title", "")
        try:
            app.config["manager"].add_task(title)
        except ValueError:
            pass
        return redirect(url_for("index"))

    @app.route("/complete/<int:task_id>", methods=["POST"])
    def complete(task_id):
        app.config["manager"].complete_task(task_id)
        return redirect(url_for("index"))

    @app.route("/delete/<int:task_id>", methods=["POST"])
    def delete(task_id):
        app.config["manager"].delete_task(task_id)
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)