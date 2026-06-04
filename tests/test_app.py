import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_index_shows_task_titles(client):
    client.post("/add", data={"title": "Помыть посуду"})
    response = client.get("/")
    assert "Помыть посуду" in response.get_data(as_text=True)

def test_add_task_via_post(client):
    response = client.post("/add", data={"title": "Новая задача"})
    assert response.status_code == 302
    page = client.get("/").get_data(as_text=True)
    assert "Новая задача" in page