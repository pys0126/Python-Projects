print("------计算器mini  由PYS制作------")
print("说明：运算范围仅支持加(+)减(-)乘(x)除(/)幂(*)")

def operation():
    while True:
        num1 = float(input("\n\t请输入第一个数字："))
        op = input("\n\t请输入运算符：")
        num2 = float(input("\n\t请输入第二个数字："))
        if op == "+":
            print(num1 + num2)
            break
        elif op == "-":
            print(num1 - num2)
            break
        elif op == "x":
            print(num1 * num2)
            break
        elif op == "/":
            print(num1 / num2)
            break
        elif op == "*":
            print(num1 ** num2)
            break
        else:
            print("输入错误，或不支持此运算，请重新输入！")

def quit():
    while True:
        Exit = input("如果要继续进行运算请按 1 反之请按 0 ：")
        if Exit == "1":
            operation()
        elif Exit == "0":
            break
        else:
            print("输入错误,请重新输入！")

#Run...
operation()
quit()






     


