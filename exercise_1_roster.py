# exercise_1_roster.py
# 学员花名册管理器

# 1. 准备一个空的花名册（字典）
roster = {}
roster["mum"] = {"email": "123@gmail.com", "date": "1/1/26"}
roster["dad"] = {"email": "234@gmail.com", "date": "1/2/26"}


# 2. 主循环：让程序一直跑
while True:
    # 3. 显示菜单
    print("请选择操作：")
    print("1. 添加学员")
    print("2. 查询学员")
    print("3. 删除学员")
    print("4. 退出")

    # 4. 接收用户输入
    choice = input("请输入选项编号：")

    # 5. 根据选择执行
    if choice == "1":
        name = input("name: ")
        email = input("email: ")
        date = input("date: ")
        roster[name] = {"email": email, "date": date}
        print("saved successfully", name)

    elif choice == "2":
        name = input("what's the name: ")
        if name in roster:
            print("found: ", roster[name])
        else:
            print("cannot find it")

    elif choice == "3":
        name = input("what's the name to delete: ")
        if name in roster:
            del roster[name]
            print("deleted", name)
        else: 
            print("cannot find it")

    elif choice == "4":
        print("bye!")
        break   # 跳出 while 循环

    else:
        print("void, please print 1-4")