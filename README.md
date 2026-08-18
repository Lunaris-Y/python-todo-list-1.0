# Python Todo List

这是一个适合 Python 初学者练习的命令行 Todo List 项目。

## 项目功能

项目包含以下功能：

1. 添加任务
2. 查看所有任务
3. 删除任务
4. 完成任务
5. 退出程序
6. 自动保存和恢复任务

添加、删除或完成任务后，程序会立即把最新的任务列表保存到本地的 `tasks.json` 文件中。重新启动程序时，之前保存的任务会被自动读取。

查看任务时，`[ ]` 表示任务尚未完成，`[✓]` 表示任务已经完成。

## 文件结构

```text
.
├── main.py       # 程序入口和菜单逻辑
├── tasks.py      # 添加、查看、删除和完成任务的逻辑
├── storage.py    # JSON 文件读取和保存逻辑
├── tests/
│   ├── test_tasks.py    # 任务功能测试
│   └── test_storage.py  # JSON 读取和保存测试
├── README.md     # 项目介绍和运行说明
├── .gitignore    # Git 不需要跟踪的文件
└── tasks.json    # 运行时生成的数据文件，不提交到 Git
```

## 运行方法

1. 确保电脑已经安装 Python 3。
2. 在命令行中进入项目目录。
3. 运行下面的命令：

```bash
python main.py
```

如果系统中的 Python 3 命令是 `python3`，则运行：

```bash
python3 main.py
```

程序启动后，输入菜单中的数字 `1`、`2`、`3`、`4` 或 `5`，再按回车键。

## 任务如何保存

程序使用 JSON 文件 `tasks.json` 保存任务。JSON 文件中的数据是一个任务列表，列表中的每个任务都包含任务名称和完成状态，例如：

```json
[
    {
        "title": "学习 Python",
        "completed": false
    },
    {
        "title": "写高数作业",
        "completed": true
    }
]
```

不需要手动创建 `tasks.json`；如果它不存在，程序仍然可以正常启动，并会在第一次添加任务时自动创建它。如果文件内容为空或 JSON 格式错误，程序会使用空任务列表继续运行。项目不读取旧版本的 `tasks.txt`。

## 项目学习目标

通过这个项目，可以学习和练习：

- Python 基础语法
- 文件读写
- JSON 数据存储
- 模块化设计
- Git 版本管理

## 开发历史

- v0.1：基础 Todo 功能
- v0.2：本地文件持久化
- v0.3：删除任务功能
- v0.4：JSON 数据结构和完成状态
- v0.5：项目结构重构
- v0.6：完善项目文档
- v0.7：增加 pytest 自动化测试
- v0.8：处理空文件和 JSON 格式错误

## Testing

安装 pytest:

```bash
pip install pytest
```

运行测试:

```bash
python -m pytest tests -v
```

测试覆盖添加、完成、删除任务、JSON 保存和读取，以及空文件和 JSON 格式错误处理。
