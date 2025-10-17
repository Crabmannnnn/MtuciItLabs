def Greetings(name):
    print("Здравствуйте,",name)
def square(number):
    print("Квадрат числа:",number**2)
def max_of_two(x,y):
    if x > y:
        print("Большое число:", x)
    elif x==y:
        print("Числа равны")
    else:
        print("Большое число:", y)

name=input("Введите имя:")
Greetings(name)
number=input("Введите число:")
try:
    number=int(number)
    square(number)
except ValueError:
    print("Это не число")
x=input("Введите первое число")
y=input("Введите второе число")
try:
    x=int(x)
    y=int(y)
    max_of_two(x,y)
except ValueError:
    print("Это не числа")
