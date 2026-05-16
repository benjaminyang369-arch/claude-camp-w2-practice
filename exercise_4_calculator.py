print("=== 安全计算器 ===")
print("支持运算：+ - * /")
print("输入 q 退出\n")

while True:
    # 第 1 步：读第一个数（可能 ValueError）
    num1_input = input("请输入第一个数（或 q 退出）：")
    if num1_input == "q":
        print("再见！")
        break
    
    try:
        num1 = float(num1_input)
    except ValueError:
        # TODO: 提示用户输入有效数字，然后 continue 回到循环开头
        print("请输入有效的数字！")
        continue

    # 第 2 步：读运算符
    op = input("请输入运算符（+ - * /）：")
    
    # 第 3 步：读第二个数（可能 ValueError）
    # TODO: 模仿第 1 步的 try/except 写
    num2_input = input("请输入第二个数：")
    try:
        num2 = float(num2_input)
    except ValueError:
        print("请输入有效的数字！")
        continue    
    
    # 第 4 步：根据运算符计算
    if op == "+":
        result = num1 + num2
    elif op == "-":
        # TODO
        result = num1 - num2
    elif op == "*":
        # TODO
        result = num1 * num2
    elif op == "/":
        # 这里要处理 ZeroDivisionError
        try:
            result = num1 / num2
        except ZeroDivisionError:
            # TODO: 提示除数不能为 0，然后 continue
            print("错误：除数不能为 0！")
            continue
    else:
        # TODO: 提示不支持的运算符，continue
        print("错误：不支持的运算符！")
        continue        
    
    # 第 5 步：打印结果
    print(f"结果：{num1} {op} {num2} = {result}\n")