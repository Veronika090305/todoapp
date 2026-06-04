from flask import Flask, request, redirect, url_for, render_template_string
from models import TaskManager

PAGE = """<!doctype html>
<html lang="ru">
<head><meta charset="utf-8"><title>Список задач</title></head>
<body>
  <h1>Список задач</h1>
  <form method="post" action="{{ url_for('add') }}">
    <input name="title" placeholder="Новая задача">
    <button type="submit">Добавить</button>
  </form>
  <ul>
    {% for task in tasks %}
    <li>{{ task.title }}</li>
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
        return render_template_string(PAGE, tasks=manager.all_tasks())

    @app.route("/add", methods=["POST"])
    def add():
        title = request.form.get("title", "")
        try:
            app.config["manager"].add_task(title)
        except ValueError:
            pass
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)