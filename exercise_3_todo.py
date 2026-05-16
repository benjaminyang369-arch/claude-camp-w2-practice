# exercise_3_todo.py
# 待办事项清单（带文件保存）

import json   # ← 新概念：导入 json 模块

# ============================================================
# 工具函数（def 是新概念）
# ============================================================

def save_todos(todos):
    """把 todos 列表保存到 todos.json 文件"""
    with open("todos.json", "w") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
        # ensure_ascii=False: 中文不会被转义成 \uXXXX
        # indent=2: 文件里换行缩进，方便人看


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
        # TODO: 把 {"task": task, "done": False} 这个字典追加到 todos 列表
        todos.append({"task": task, "done": False})
        # 提示：用 .append() 方法
        save_todos(todos)
        # TODO: 调用 save_todos(todos) 保存到文件
        print(f"已添加：{task}")
    
    # ---------- 完成待办 ----------
    elif choice == "2":
        if len(todos) == 0:
            print("清单是空的，没有可完成的待办")
        else:
            # 先把清单显示一遍，让用户看到序号
            for i, todo in enumerate(todos):
                # enumerate(): 同时拿到「索引 i」和「元素 todo」
                # i 从 0 开始，所以显示给用户的序号是 i+1
                status = "[√]" if todo["done"] else "[ ]"
                print(f"{i+1}. {status} {todo['task']}")
            
            # 让用户输入要完成的序号
            try:
                num = int(input("请输入要完成的序号："))
                # TODO: 把列表里第 (num-1) 个待办的 done 改成 True
                # 提示：todos[num - 1]["done"] = ???
                todos[num - 1]["done"] = True
                save_todos(todos)
                print(f"已完成：{todos[num - 1]['task']}")
                # TODO: 调用 save_todos(todos) 保存
            except ValueError:
                # 用户输入了非数字（比如 "abc"），int() 转换失败
                print("请输入数字！")
            except IndexError:
                # 用户输入的序号超出范围（比如清单只有 3 个，输入 10）
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