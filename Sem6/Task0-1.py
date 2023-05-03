# определить простое ли число или нет

number = int(input("enter: "))
def Simple (number, divider):
    if divider == 1:
        return "yes"
    elif number % divider == 0:
        return "no"
    else:
        return Simple(number, divider - 1)

print(Simple(number, number // 2))