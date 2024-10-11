first = int(input("Введите первое число: "))
sekond = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first==sekond and sekond==third:
    print("3")
elif first==sekond or sekond==third or first==third:
    print("2")
else: print("0")