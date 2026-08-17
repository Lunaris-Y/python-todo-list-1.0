TASKS_FILE = "tasks.txt"


def load_tasks():
    """从本地文件读取任务。"""
    tasks = []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.rstrip("\n"))
    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    """把所有任务保存到本地文件。"""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    """添加一个任务并立即保存。"""
    task = input("请输入任务内容：")

    if task == "":
        print("任务内容不能为空！")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("任务添加成功！")


def view_tasks(tasks):
    """查看所有任务。"""
    if len(tasks) == 0:
        print("目前没有任务。")
    else:
        print("\n所有任务：")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def main():
    """运行 Todo List 程序。"""
    tasks = load_tasks()

    while True:
        print("\n--- Todo List ---")
        print("1. 添加任务")
        print("2. 查看所有任务")
        print("3. 退出程序")

        choice = input("请选择功能（1/2/3）：")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("程序已退出。")
            break
        else:
            print("输入无效，请输入 1、2 或 3。")


if __name__ == "__main__":
    main()
