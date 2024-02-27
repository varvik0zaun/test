from random import randint
pc=randint(1,500)
bro=int(input("Угадайте целое число от 1 до 500:"))
while bro!=pc:
    bro=int(input("еще раз:"))
    if bro<pc:
        print("Ваше число меньше, чем задумал компьютер")
    elif bro>pc:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print("Вы угадали")
print(bro)
print(pc)