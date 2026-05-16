# exercise_3_todo.py
# 待办事项清单（带文件保存）

import json   # 导入 json 模块


def save_todos(todos):
    """把 todos 列表保存到 todos.json 文件"""
    with open("todos.json", "w") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def load_todos():
    """从 todos.json 加载，如果文件不存在就返回空列表"""
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# ============================================================
# 主程序
# ============================================================

# 启动时加载历史数据
todos = load_todos()

while True:
    print("\n请选择操作：")
    print("1. 添加待办")
    print("2. 完成待办")
    print("3. 查看清单")
    print("4. 退出")
    
    choice = input("请输入选项编号：")
    
    # ---------- 添加待办 ----------
    if choice == "1":
        task = input("请输入待办内容：")
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print(f"已添加：{task}")
    
    # ---------- 完成待办 ----------
    elif choice == "2":
        if len(todos) == 0:
            print("清单是空的，没有可完成的待办")
        else:
            for i, todo in enumerate(todos):
                status = "[√]" if todo["done"] else "[ ]"
                print(f"{i+1}. {status} {todo['task']}")
            
            try:
                num = int(input("请输入要完成的序号："))
                todos[num - 1]["done"] = True
                save_todos(todos)
                print(f"已完成：{todos[num - 1]['task']}")

            except ValueError:
                print("请输入数字！")
            except IndexError:
                print("序号超出范围！")
    
    # ---------- 查看清单 ----------
    elif choice == "3":
        if len(todos) == 0:
            print("清单是空的")
        else:
            for i, todo in enumerate(todos):
                status = "[√]" if todo["done"] else "[ ]"
                print(f"{i+1}. {status} {todo['task']}")
    
    # ---------- 退出 ----------
    elif choice == "4":
        print("再见！")
        break
    
    else:
        print("无效选项，请输入 1-4")