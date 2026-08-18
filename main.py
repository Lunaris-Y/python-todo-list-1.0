from storage import load_tasks
from tasks import add_task, complete_task, delete_task, view_tasks


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
