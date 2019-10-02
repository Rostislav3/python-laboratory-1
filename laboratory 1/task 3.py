print("Салтиков А.В \nЛабораторна робота №1 \nВаріант 19 \nОбчислення функції в залежності від значень x.  \n")
import math
x = float(input("Введіть x\n"))

if x>-4:
    x = math.cos(2*x)+9
    print(x)
else:
    x = ((math.cos(x))/x-9)*-1
    print(x)
