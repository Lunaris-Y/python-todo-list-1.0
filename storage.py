import json


TASKS_FILE: str = "tasks.json"


def load_tasks() -> list[dict]:
    """从 JSON 文件读取任务。"""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: list[dict]) -> None:
    """把所有任务保存到 JSON 文件。"""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
