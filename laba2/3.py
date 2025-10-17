def is_prime(number):
    for x in range(2, number+1):
        if x<number and number%x==0:
            return False
        else:
            ++x
    return True
number=input("Введите число")
try:
    number=int(number)
    if is_prime(number)==True:
        print("Это простое число")
    else:
        print("Это не простое число")
except ValueError:
    print("Это не число")
