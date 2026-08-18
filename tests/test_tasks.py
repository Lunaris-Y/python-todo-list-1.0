import tasks


def test_add_task_increases_task_count(monkeypatch):
    task_list = []

    monkeypatch.setattr("builtins.input", lambda prompt: "学习 Python")
    monkeypatch.setattr(tasks, "save_tasks", lambda task_list: None)

    tasks.add_task(task_list)

    assert len(task_list) == 1


def test_add_task_has_correct_title(monkeypatch):
    task_list = []

    monkeypatch.setattr("builtins.input", lambda prompt: "学习 Python")
    monkeypatch.setattr(tasks, "save_tasks", lambda task_list: None)

    tasks.add_task(task_list)

    assert task_list[0]["title"] == "学习 Python"


def test_complete_task_changes_completed_to_true(monkeypatch):
    task_list = [
        {
            "title": "学习 Python",
            "completed": False
        }
    ]

    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    monkeypatch.setattr(tasks, "save_tasks", lambda task_list: None)

    tasks.complete_task(task_list)

    assert task_list[0]["completed"] is True


def test_delete_task_decreases_task_count(monkeypatch):
    task_list = [
        {
            "title": "学习 Python",
            "completed": False
        }
    ]

    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    monkeypatch.setattr(tasks, "save_tasks", lambda task_list: None)

    tasks.delete_task(task_list)

    assert len(task_list) == 0
