import json


TASKS_FILE = "tasks.json"


def load_tasks():
    """从 JSON 文件读取任务。"""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """把所有任务保存到 JSON 文件。"""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(tasks):
    """添加一个任务并立即保存。"""
    task = input("请输入任务内容：")

    if task == "":
        print("任务内容不能为空！")
        return

    new_task = {
        "title": task,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("任务添加成功！")


def view_tasks(tasks):
    """查看所有任务。"""
    if len(tasks) == 0:
        print("目前没有任务。")
    else:
        print("\n所有任务：")
        for number, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "✓"
            else:
                status = " "
            print(f"{number}. [{status}] {task['title']}")


def delete_task(tasks):
    """根据任务编号删除任务并立即保存。"""
    if len(tasks) == 0:
        print("任务列表为空，无法删除")
        return

    view_tasks(tasks)
    user_input = input("请输入要删除的任务编号：")

    try:
        number = int(user_input)
    except ValueError:
        print("编号不存在，无法删除")
        return

    if number < 1 or number > len(tasks):
        print("编号不存在，无法删除")
        return

    del tasks[number - 1]
    save_tasks(tasks)
    print("任务删除成功！")


def complete_task(tasks):
    """根据任务编号完成任务并立即保存。"""
    if len(tasks) == 0:
        print("任务列表为空，无法完成")
        return

    view_tasks(tasks)
    user_input = input("请输入要完成的任务编号：")

    try:
        number = int(user_input)
    except ValueError:
        print("编号不存在，无法完成")
        return

    if number < 1 or number > len(tasks):
        print("编号不存在，无法完成")
        return

    task = tasks[number - 1]

    if task["completed"]:
        print("任务已经完成。")
        return

    task["completed"] = True
    save_tasks(tasks)
    print("任务已完成！")


def main():
    """运行 Todo List 程序。"""
    tasks = load_tasks()

    while True:
        print("\n--- Todo List ---")
        print("1. 添加任务")
        print("2. 查看所有任务")
        print("3. 删除任务")
        print("4. 完成任务")
        print("5. 退出程序")

        choice = input("请选择功能（1/2/3/4/5）：")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("程序已退出。")
            break
        else:
            print("输入无效，请输入 1、2、3、4 或 5。")


if __name__ == "__main__":
    main()
