# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def myue(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            myue = i
    return  myue
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(num1,"和",num2, "的最大公约数为", myue(num1, num2))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
