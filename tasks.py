from storage import save_tasks


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
