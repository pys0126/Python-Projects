import random
st = random.randint(1,100)
print("\t\t由PYS制作")
str1 = input("\t猜猜我现在心里想的什么数字:")
str2 = int(str1)
while str2 != 101:
    str1 = input("请再猜一次呀:")
    str2 = int(str1)
    if str2 == st:
        print("哟,真强呢!")
    else:
        if str2 > st:
            print("数字大了哦")
        else:
            print("数字小了哦")
print("猜对了呀!")
print("see you!")
