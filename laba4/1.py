import math
import datetime
try:
    number=float(input("введите число"))
    print("Квадратный корень числа:",math.sqrt(number))
except ValueError:
    print("Некоректное число")
dt_now=datetime.datetime.now()
print("Текущее время:",dt_now)
