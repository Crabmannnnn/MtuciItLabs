def Greetings(name):
    print("Здравствуйте,",name)
def square(number):
    return(number**2) 
def max_of_two(x,y):
    if x > y:
        return(x) 
    elif x==y:
        return("числа равны") 
    else:
        return(y) 

name=input("Введите имя:")
Greetings(name)
number=input("Введите число:")
try:
    number=int(number)
     print(square(number)) 
except ValueError:
    print("Это не число")
x=input("Введите первое число")
y=input("Введите второе число")
try:
    x=int(x)
    y=int(y)
    print(max_of_two(x,y)) 
except ValueError:
    print("Это не числа")
