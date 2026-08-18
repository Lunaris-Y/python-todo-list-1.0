import storage


def test_save_tasks_creates_json_file(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    task_list = [
        {
            "title": "学习 Python",
            "completed": False
        }
    ]

    monkeypatch.setattr(storage, "TASKS_FILE", test_file)

    storage.save_tasks(task_list)

    assert test_file.exists()


def test_load_tasks_returns_same_data(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    expected_tasks = [
        {
            "title": "学习 Python",
            "completed": False
        }
    ]

    monkeypatch.setattr(storage, "TASKS_FILE", test_file)
    storage.save_tasks(expected_tasks)

    actual_tasks = storage.load_tasks()

    assert actual_tasks == expected_tasks


def test_load_tasks_returns_empty_list_for_empty_file(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    test_file.write_text("", encoding="utf-8")

    monkeypatch.setattr(storage, "TASKS_FILE", test_file)

    assert storage.load_tasks() == []


def test_load_tasks_returns_empty_list_for_invalid_json(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    test_file.write_text("{错误的 JSON", encoding="utf-8")

    monkeypatch.setattr(storage, "TASKS_FILE", test_file)

    assert storage.load_tasks() == []
